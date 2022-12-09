from typing import Any
from unittest import TestCase

from main import BlenderData


class TestBlenderData(TestCase):
    blender_data: BlenderData

    def setUp(self) -> None:
        self.blender_data = BlenderData()

    def test_entries(self):
        entries: dict[str, Any] = self.blender_data.entries
        with self.subTest("No entries after initialization"):
            self.assertEqual({}, entries)
        with self.subTest("Returned entries is a copy, not a referance"):
            entries["New entry"] = {}
            self.assertNotEqual(entries, self.blender_data.entries)
        with self.subTest("__setitem__ works"):
            self.blender_data["test"] = 42
            self.assertEqual({"test": 42}, self.blender_data.entries)
