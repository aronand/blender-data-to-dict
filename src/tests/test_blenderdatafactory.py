from random import choice
from unittest import TestCase

from blenderdata import BlenderDataFactory, BlenderMesh, BlenderObject


class TestBlenderDataFactory(TestCase):
    objects: list[BlenderObject]
    new_objects: list[BlenderObject]
    names: list[str] = [f"Test{i}" for i in range(9)]

    def setUp(self) -> None:
        self.objects = []
        for name in self.names:
            blender_object: BlenderObject = BlenderObject()
            blender_object.name = name
            blender_object.type = choice(["EMPTY", "MESH"])
            if blender_object.type == "MESH":
                mesh: BlenderMesh = BlenderMesh()
                mesh.name = name
                blender_object.data = mesh
            self.objects.append(blender_object)
        self.new_objects = [obj for obj in BlenderDataFactory.blender_object_generator(self.objects)]

    def test_generator(self):
        with self.subTest("Objects are unique"):
            for idx in range(len(self.objects)):
                self.assertIsNot(self.objects[idx], self.new_objects[idx])
        with self.subTest("Objects in iterable must implement BlenderObjectProtocol (raises TypeError)"):
            mesh: BlenderMesh = BlenderMesh()
            mesh.name = "i_should_fail"
            with self.assertRaises(TypeError):
                a = next(BlenderDataFactory.blender_object_generator([mesh]))

    def test_get_blender_object(self):
        with self.subTest("Returned object has correct data"):
            for idx in range(len(self.objects)):
                original: BlenderObject = self.objects[idx]
                created: BlenderObject = self.new_objects[idx]
                self.assertEqual(original.name, created.name)
                self.assertEqual(original.type, created.type)
                if original.data is None:
                    continue
                self.assertIsNot(original.data, created.data)
        with self.subTest("Returned object is unique"):
            # NOTE: If this fails, the generator most likely fails as well
            for idx in range(len(self.objects)):
                original: BlenderObject = self.objects[idx]
                created: BlenderObject = self.new_objects[idx]
                self.assertIsNot(original, created)

    def test_get_blender_mesh(self):
        mesh: BlenderMesh = BlenderMesh()
        mesh.name = "test.mesh"
        new_mesh: BlenderMesh = BlenderDataFactory.get_blender_mesh(mesh)
        with self.subTest("Returned mesh has correct data"):
            self.assertEqual(mesh.name, new_mesh.name)
        with self.subTest("Returned mesh is a unique object"):
            self.assertIsNot(mesh, new_mesh)
