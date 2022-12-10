from typing import Any
from unittest import TestCase

from main import BlenderObjects

from tests.mock_classes import MockMaterialSlot, MockMesh, MockModifier, MockObject


class TestBlenderObjects(TestCase):
    blender_objects: BlenderObjects
    mock_objects: list[MockObject] = [
        MockObject("Cube", "MESH"),
        MockObject("Cube.001", "MESH")
    ]
    mock_entry: dict[str, Any] = {
        "type": "MESH", "data": "Cube", "modifiers": [{"type": "SUBSURF"}], "materials": ["Material"]
    }

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
            mock_object: MockObject = MockObject("", "MESH")
            mock_object.data = MockMesh("Cube")
            mock_object.modifiers.append(MockModifier("SUBSURF"))
            mock_object.material_slots.append((MockMaterialSlot("Material")))
            entry: dict[str, Any] = self.blender_objects.create_object_entry(mock_object)
            self.assertEqual(self.mock_entry, entry)
