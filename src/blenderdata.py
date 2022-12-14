import bpy
from typing import Any


class BlenderData:
    @classmethod
    def objects_dict(cls) -> dict[str, Any]:
        obj: bpy.types.Object
        objects: dict[str, Any] = {}
        for obj in bpy.data.objects:
            data: str | None = (None if obj.data is None else obj.data.name)
            objects[obj.name] = {
                "type": obj.type,
                "data": data,
                "modifiers": [mod.type for mod in obj.modifiers],
                "material_slots": [mat.name for mat in obj.material_slots]
            }
        return objects

    @classmethod
    def mesh_dict(cls) -> dict[str, Any]:
        mesh: bpy.types.Mesh
        meshes: dict[str, Any] = {}
        for mesh in bpy.data.meshes:
            meshes[mesh.name] = {}
        return meshes

    @classmethod
    def materials_dict(cls) -> dict[str, Any]:
        material: bpy.types.Material
        materials: dict[str, Any] = {}
        for material in bpy.data.materials:
            materials[material.name] = {}
        return materials

    @classmethod
    def images_dict(cls) -> dict[str, Any]:
        image: bpy.types.Image
        images: dict[str, Any] = {}
        for image in bpy.data.images:
            images[image.name] = {}
        return images

    @classmethod
    def dict(cls) -> dict[str, Any]:
        """Returns everything in a single dictionary. Must be defined after all the classmethods it calls!"""
        return {
            "objects": cls.objects_dict(),
            "meshes": cls.mesh_dict(),
            "materials": cls.materials_dict(),
            "images": cls.images_dict()
        }


if __name__ == "__main__":
    raise RuntimeError("This module should only be imported")
