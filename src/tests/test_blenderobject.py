from unittest import TestCase

from blenderdata import BlenderMesh, BlenderObject, BlenderObjectProtocol


class TestBlenderObject(TestCase):
    blender_object: BlenderObject
    mesh: BlenderMesh

    def setUp(self) -> None:
        self.blender_object = BlenderObject()
        self.mesh = BlenderMesh()
        self.mesh.name = "test"

    def test_initialization(self):
        with self.subTest("Initialized object is empty"):
            self.assertEqual("", self.blender_object.name)
            self.assertEqual("", self.blender_object.type)
            self.assertEqual(None, self.blender_object.data)
            self.assertEqual([], self.blender_object.modifiers)
            self.assertEqual([], self.blender_object.material_slots)

    def test_type_property(self):
        with self.subTest("Setter: Type must be str (raises TypeError)"):
            with self.assertRaises(TypeError):
                self.blender_object.type = 42
        with self.subTest("Setter: Value can't be an empty string (raises ValueError)"):
            with self.assertRaises(ValueError):
                self.blender_object.type = ""
        with self.subTest("Setter/Getter: When given a valid value, value can be set and retrieved"):
            type_name: str = "test"
            self.blender_object.type = type_name
            self.assertEqual(type_name, self.blender_object.type)

    def test_protocol_implementation(self):
        with self.subTest("BlenderObject implements BlenderObjectProtocol"):
            self.assertTrue(isinstance(self.blender_object, BlenderObjectProtocol))
