"""Module holding the BlenderData class, used to turn bpy.data into a dictionary."""
from typing import Any

import bpy


class BlenderData:
    """A static class used to get a dictionary of Blender data.

    Can be used to return specific dictionaries (e.g. objects, materials, etc.) or
    everything as single dictionary
    """
    @classmethod
    def objects_dict(cls) -> dict[str, Any]:
        """Returns a dictionary of bpy.data.objects."""
        obj: bpy.types.Object
        objects: dict[str, Any] = {}
        for obj in bpy.data.objects:
            data: str | None = (None if obj.data is None else obj.data.name)
            objects[obj.name] = {
                "data": data,
                "material_slots": [mat.name for mat in obj.material_slots],
                "modifiers": [mod.type for mod in obj.modifiers],
                "type": obj.type,
            }
        return objects

    @classmethod
    def meshes_dict(cls) -> dict[str, Any]:
        """Returns a dictionary of bpy.data.meshes."""
        mesh: bpy.types.Mesh
        meshes: dict[str, Any] = {}
        for mesh in bpy.data.meshes:
            mesh.calc_loop_triangles()  # must be called before we access mesh.loop_triangles
            meshes[mesh.name] = {
                "edges": len(mesh.edges),  # 1 edge = 2 vertices
                "loops": len(mesh.loops),  # 1 loop = 1 edge, 1 vert
                "polygons": len(mesh.polygons),  # 1 polygon = n loops
                "loop_triangles": len(mesh.loop_triangles),
                "vertices": len(mesh.vertices),
            }
        return meshes

    @classmethod
    def materials_dict(cls) -> dict[str, Any]:
        """Returns a dictionary of bpy.data.materials."""
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
        """Returns a dictionary of nodes in a material's node_tree.

        :param material: A bpy.types.Material object
        """
        nodes: dict[str, Any] = {}
        if material.node_tree is None:
            return nodes
        for node in material.node_tree.nodes:
            node_data: dict[str, Any] = {
                "type": node.type
            }
            if isinstance(node, bpy.types.ShaderNodeTexImage):
                node_data["image"] = node.image.name
            nodes[node.name] = node_data
        return nodes

    @classmethod
    def images_dict(cls) -> dict[str, Any]:
        """Returns a dictionary of bpy.data.images."""
        image: bpy.types.Image
        images: dict[str, Any] = {}
        for image in bpy.data.images:
            images[image.name] = {
                "channels": image.channels,
                "depth": image.depth,
                "file_format": image.file_format,
                "filepath": image.filepath,
                "size": list(image.size),
                "source": image.source,
                "type": image.type,
            }
        return images

    @classmethod
    def scenes_dict(cls) -> dict[str, Any]:
        """Returns a dictionary of bpy.data.scenes."""
        scenes: dict[str, Any] = {}
        for scene in bpy.data.scenes:
            scenes[scene.name] = {
                "objects": [obj.name for obj in scene.objects],
                "view_layers": [layer.name for layer in scene.view_layers],
            }
        return scenes

    @classmethod
    def dict(cls) -> dict[str, Any]:
        """Returns everything in a single dictionary."""
        # Note: Must be defined after all the methods it calls
        return {
            "images": cls.images_dict(),
            "materials": cls.materials_dict(),
            "meshes": cls.meshes_dict(),
            "objects": cls.objects_dict(),
            "scenes": cls.scenes_dict(),
        }


if __name__ == "__main__":
    raise RuntimeError("This module should only be imported")
