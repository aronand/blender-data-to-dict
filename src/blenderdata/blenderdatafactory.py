from typing import Callable, Generator, Iterable

from .blendermesh import BlenderMesh
from .blendermeshprotocol import BlenderMeshProtocol
from .blenderobject import BlenderObject
from .blenderobjectprotocol import BlenderObjectProtocol


class BlenderDataFactory:
    @classmethod
    def get_blender_object(cls, obj: BlenderObjectProtocol) -> BlenderObject:
        data_function: dict[str, Callable] = {
            "MESH": cls.get_blender_mesh
        }
        new_object: BlenderObject = BlenderObject()
        new_object.name = obj.name
        new_object.type = obj.type
        new_object.data = data_function.get(obj.type, lambda _: None)(obj)
        return new_object

    @classmethod
    def get_blender_mesh(cls, mesh: BlenderMeshProtocol) -> BlenderMesh:
        new_mesh: BlenderMesh = BlenderMesh()
        new_mesh.name = mesh.name
        return new_mesh

    @classmethod
    def blender_object_generator(cls, objects: Iterable[BlenderObjectProtocol]) -> Generator[BlenderObject, None, None]:
        """Generate BlenderObjects from an iterable with objects that implement BlenderObjectProtocol
         (e.g. bpy.data.Objects).

         :raises TypeError: Object in iterable doesn't implement BlenderObjectProtocol.
         """
        for obj in objects:
            if not isinstance(obj, BlenderObjectProtocol):
                raise TypeError
            new_object: BlenderObject = cls.get_blender_object(obj)
            yield new_object
