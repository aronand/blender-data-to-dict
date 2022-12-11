from typing import Any
from unittest import TestCase

from blenderdata import BlenderObject, blender_object_generator, BlenderObjectProtocol


class TestBlenderObject(TestCase):
    blender_object: BlenderObject
    mock_dict: dict[str, Any] = {
        "test": {
            "type": "MESH",
            "data": 0,
            "modifiers": [],
            "material_slots": []
        }
    }

    def setUp(self) -> None:
        self.blender_object = BlenderObject()

    def test_initialization(self):
        with self.subTest("Initialized object is empty"):
            self.assertEqual("", self.blender_object.name)
            self.assertEqual("", self.blender_object.type)
            self.assertEqual(0, self.blender_object.data)
            self.assertEqual([], self.blender_object.modifiers)
            self.assertEqual([], self.blender_object.material_slots)
        with self.subTest("Object can be initialized by another object compliant with BlenderObjectProtocol"):
            bl_obj: BlenderObject = BlenderObject()
            bl_obj.name = "test"
            bl_obj.type = "MESH"
            self.blender_object.init_from_object(bl_obj)
            self.assertEqual("test", self.blender_object.name)
            self.assertEqual("MESH", self.blender_object.type)

    def test_name_property(self):
        with self.subTest("Setter: Type must be str (raises TypeError)"):
            with self.assertRaises(TypeError):
                self.blender_object.name = 42
        with self.subTest("Setter: Value can't be an empty string (raises ValueError)"):
            with self.assertRaises(ValueError):
                self.blender_object.name = ""
        with self.subTest("Setter/Getter: When given a valid value, value can be set and retrieved"):
            name: str = "test"
            self.blender_object.name = name
            self.assertEqual(name, self.blender_object.name)

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

    def test_dict_property(self):
        bl_obj: BlenderObject = BlenderObject()
        name: str = "test"
        bl_obj.name = name
        bl_obj.type = self.mock_dict[name]["type"]
        self.assertEqual(self.mock_dict, bl_obj.dict)


class TestBlenderObjectGenerator(TestCase):
    objects: list[BlenderObject]
    names: list[str] = [f"Test{i}" for i in range(9)]

    def setUp(self) -> None:
        self.objects = []
        for name in self.names:
            blender_object: BlenderObject = BlenderObject()
            blender_object.name = name
            blender_object.type = "EMPTY"
            self.objects.append(blender_object)

    def test_generator(self):
        with self.subTest("Names match"):
            names: list[str] = [obj.name for obj in blender_object_generator(self.objects)]
            self.assertEqual(names, self.names)
