from unittest import TestCase

from blenderdata import BlenderMesh, BlenderMeshProtocol


class TestBlenderMesh(TestCase):
    mesh: BlenderMesh

    def setUp(self) -> None:
        self.mesh = BlenderMesh()

    def test_protocol_implementation(self):
        with self.subTest("BlenderMesh implements BlenderMeshProtocol"):
            self.assertTrue(isinstance(self.mesh, BlenderMeshProtocol))
