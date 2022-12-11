from typing import Any, Callable

from .blendermeshprotocol import BlenderMeshProtocol
from .blenderobjectprotocol import BlenderObjectProtocol


class BlenderDataDict:
    @classmethod
    def get_dict(cls, obj: Any) -> dict:
        __types: dict[str, Callable[..., dict[str, Any]]] = {
            "Object": cls.get_object_dict,
            "Mesh": cls.get_mesh_dict
        }
        data: dict = {}
        obj_type: str = type(obj).__name__
        for T, func in __types.items():
            if not obj_type.endswith(T):
                continue
            data = func(obj)
        return data

    @classmethod
    def get_object_dict(cls, obj: BlenderObjectProtocol) -> dict[str, Any]:
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
    def get_mesh_dict(cls, mesh: BlenderMeshProtocol) -> dict[str, Any]:
        return {mesh.name: {}}
