from typing import Any

from unittest import TestCase

from blenderdata import BlenderDataDict, BlenderMesh, BlenderObject


class TestBlenderDataDict(TestCase):
    blender_object: BlenderObject
    mesh: BlenderMesh

    object_dict: dict[str, Any]
    mesh_dict: dict[str, Any] = {"test": {}}

    def setUp(self) -> None:
        self.blender_object = BlenderObject()
        self.blender_object.name = "test"
        self.blender_object.type = "EMPTY"
        self.mesh = BlenderMesh()
        self.mesh.name = "test"
        self.object_dict: dict[str, Any] = {
            "test": {
                "type": "EMPTY",
                "data": None,
                "modifiers": [],
                "material_slots": []
            }
        }

    def test_get_dict(self):
        with self.subTest("None returns an empty dict"):
            self.assertEqual({}, BlenderDataDict.get_dict(None))
        with self.subTest("BlenderObject returns a correct dict"):
            self.assertEqual(self.object_dict, BlenderDataDict.get_dict(self.blender_object))
        with self.subTest("BlenderMesh returns a correct dict"):
            self.assertEqual(self.mesh_dict, BlenderDataDict.get_dict(self.mesh))

    def test_get_object_dict(self):
        bl_obj: BlenderObject = BlenderObject()
        bl_obj.name = "test"
        bl_obj.type = self.object_dict[bl_obj.name]["type"]
        with self.subTest("When object type == 'EMPTY', data is None"):
            self.assertEqual(self.object_dict, BlenderDataDict.get_object_dict(bl_obj))
        with self.subTest("When object type != 'EMPTY', data is str"):
            bl_obj.type = "MESH"
            bl_obj.data = self.mesh
            self.object_dict[bl_obj.name]["type"] = bl_obj.type
            self.object_dict[bl_obj.name]["data"] = bl_obj.data.name
            self.assertEqual(self.object_dict, BlenderDataDict.get_object_dict(bl_obj))

    def test_get_mesh_dict(self):
        self.assertEqual({self.mesh.name: {}}, BlenderDataDict.get_mesh_dict(self.mesh))
