from unittest import TestCase

from blenderdata import BlenderDataBaseClass


class TestBlenderDataBaseClass(TestCase):
    def setUp(self) -> None:
        self.data: BlenderDataBaseClass = BlenderDataBaseClass()

    def test_name_property(self):
        with self.subTest("Object name initializes to an empty string"):
            self.assertEqual("", self.data.name)
        with self.subTest("Setter: Type must be str (raises TypeError)"):
            with self.assertRaises(TypeError):
                self.data.name = 42
        with self.subTest("Setter: Value can't be an empty string (raises ValueError)"):
            with self.assertRaises(ValueError):
                self.data.name = ""
        with self.subTest("Setter/Getter: When given a valid value, value can be set and retrieved"):
            name: str = "test"
            self.data.name = name
            self.assertEqual(name, self.data.name)

    def test_dict_property(self):
        with self.subTest("dict property is not implemented (raises NotImplementedError"):
            with self.assertRaises(NotImplementedError):
                a = self.data.dict
