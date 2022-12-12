from typing import Any, Callable

import utils

import bpy


class BlenderDataDict:
    @classmethod
    def get_dict(cls, obj: bpy.types.ID) -> dict:
        if not isinstance(obj, bpy.types.ID):
            raise TypeError
        __types: dict[str, Callable[..., dict[str, Any]]] = {
            "Object": cls.get_object_dict,
            "Mesh": cls.get_mesh_dict
        }
        obj_type: str = utils.get_class_name(obj)
        return __types.get(obj_type, lambda _: None)(obj)

    @classmethod
    def get_object_dict(cls, obj: bpy.types.Object) -> dict[str, Any]:
        if not isinstance(obj, bpy.types.Object):
            raise TypeError
        data: str | None = (None if obj.data is None else obj.data.name)
        return {
            obj.name: {
                "type": obj.type,
                "data": data,
                "modifiers": [mod.type for mod in obj.modifiers],
                "material_slots": [mat.name for mat in obj.material_slots]
            }
        }

    @classmethod
    def get_mesh_dict(cls, mesh: bpy.types.Mesh) -> dict[str, Any]:
        if not isinstance(mesh, bpy.types.Mesh):
            raise TypeError
        return {mesh.name: {}}
