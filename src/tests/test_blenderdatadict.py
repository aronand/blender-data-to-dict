from unittest import TestCase

from blenderdata import BlenderDataDict, BlenderMesh, BlenderObject


class TestBlenderDataDict(TestCase):
    blender_object: BlenderObject
    mesh: BlenderMesh

    def setUp(self) -> None:
        self.blender_object = BlenderObject()
        self.mesh = BlenderMesh()

    def test_get_dict(self):
        with self.subTest("None returns an empty dict"):
            self.assertEqual({}, BlenderDataDict.get_dict(None))
        with self.subTest("BlenderObject returns a correct dict"):
            self.fail()
        with self.subTest("BlenderMesh returns a correct dict"):
            self.fail()

    def test_get_object_dict(self):
        self.fail()

    def test_get_mesh_dict(self):
        self.fail()
