from typing import Any
from unittest import TestCase

from blenderdata import BlenderMesh


class TestBlenderMesh(TestCase):
    mock_dict: dict[str, Any] = {"test": {}}
    mesh: BlenderMesh

    def setUp(self) -> None:
        self.mesh = BlenderMesh()

    def test_dict(self):
        self.mesh.name = "test"
        self.assertEqual(self.mock_dict, self.mesh.dict)
