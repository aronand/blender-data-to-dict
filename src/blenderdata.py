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
                "data": data,
                "material_slots": [mat.name for mat in obj.material_slots],
                "modifiers": [mod.type for mod in obj.modifiers],
                "statistics": cls.__get_object_stats(obj),
                "type": obj.type,
            }
        return objects

    @classmethod
    def __get_object_stats(cls, obj: bpy.types.Object) -> dict[str, int]:
        pass

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
            materials[material.name] = {
                "node_tree": {
                    "nodes": cls.__get_node_tree_nodes(material)
                }
            }
        return materials

    @classmethod
    def __get_node_tree_nodes(cls, material: bpy.types.Material) -> dict[str, Any]:
        nodes: dict[str, Any] = {}
        if material.node_tree is None:
            return nodes
        for node in material.node_tree.nodes:
            node_data: dict[str, Any] = {
                "type": node.type
            }
            if type(node) is bpy.types.ShaderNodeTexImage:
                node_data["image"] = node.image.name
            nodes[node.name] = node_data
        return nodes

    @classmethod
    def images_dict(cls) -> dict[str, Any]:
        image: bpy.types.Image
        images: dict[str, Any] = {}
        for image in bpy.data.images:
            images[image.name] = {
                "channels": image.channels,
                "depth": image.depth,
                "file_format": image.file_format,
                "filepath": image.filepath,
                "size": [dimension for dimension in image.size],
                "source": image.source,
                "type": image.type,
            }
        return images

    @classmethod
    def scene_stats_dict(cls) -> dict[str, int]:
        pass

    @classmethod
    def dict(cls) -> dict[str, Any]:
        """Returns everything in a single dictionary. Must be defined after all the classmethods it calls!"""
        return {
            "images": cls.images_dict(),
            "materials": cls.materials_dict(),
            "meshes": cls.mesh_dict(),
            "objects": cls.objects_dict(),
            "scene_stats": cls.scene_stats_dict(),
        }


if __name__ == "__main__":
    raise RuntimeError("This module should only be imported")
