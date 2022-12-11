from typing import Any
from unittest import TestCase

from blenderdata import BlenderMesh, BlenderMeshProtocol


class TestBlenderMesh(TestCase):
    mock_dict: dict[str, Any] = {"test": {}}
    mesh: BlenderMesh

    def setUp(self) -> None:
        self.mesh = BlenderMesh()

    def test_dict(self):
        self.mesh.name = "test"
        self.assertEqual(self.mock_dict, self.mesh.dict)

    def test_protocol_implementation(self):
        with self.subTest("BlenderMesh implements BlenderMeshProtocol"):
            self.assertTrue(isinstance(self.mesh, BlenderMeshProtocol))
