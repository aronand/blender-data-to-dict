from typing import Any, Callable
from unittest import TestCase

from main import BlenderObjects


class MockBlenderObject:
    class MockDataObject:
        def __init__(self, name: str):
            self.name = name

    def __init__(self, name: str, obj_type: str, data_name: str):
        self.name = name
        self.type = obj_type
        self.data = MockBlenderObject.MockDataObject(data_name)


class TestBlenderObjects(TestCase):
    blender_objects: BlenderObjects
    mock_object: Callable = MockBlenderObject
    mock_objects: list[MockBlenderObject] = [
        mock_object("Cube", "MESH", "Cube"),
        mock_object("Cube.001", "MESH", "Cube.001")
    ]
    mock_entry: dict[str, Any] = {"type": "MESH", "data": "Cube"}

    @property
    def mock_entries_output(self) -> dict[str, Any]:
        entries: dict[str, Any] = {}
        for obj in self.mock_objects:
            entries[obj.name] = self.blender_objects.create_object_entry(obj)
        return entries

    def setUp(self) -> None:
        self.blender_objects = BlenderObjects(self.mock_objects)

    def test_entries(self):
        with self.subTest("Entries get initialized correctly"):
            self.assertEqual(self.mock_entries_output, self.blender_objects.entries)

    def test_create_object_entry(self):
        # NOTE: If this fails, mock_entries_output will most likely cause a failure in test_entries as well!
        with self.subTest("Returned dict matches mock_entry"):
            entry: dict[str, Any] = self.blender_objects.create_object_entry(self.mock_object("", "MESH", "Cube"))
            self.assertEqual(self.mock_entry, entry)
