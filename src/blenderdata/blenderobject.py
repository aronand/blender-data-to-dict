from typing import Any, Generator, Iterable

from . import utils
from .blenderdatabaseclass import BlenderDataBaseClass
from .blenderobjectprotocol import BlenderObjectProtocol
from .blendermeshprotocol import BlenderMeshProtocol


class BlenderObject(BlenderDataBaseClass):
    """Imitates bpy.types.Object. Compliant with BlenderObjectProtocol."""
    __slots__ = "__type", "__data", "__modifiers", "__material_slots"

    def __init__(self):
        super().__init__()
        self.__type: str = ""  # type should never be "", treat as error
        self.__data: BlenderMeshProtocol | None = None
        self.__modifiers: list = []  # TODO: Modifier class and protocol
        self.__material_slots: list = []  # TODO: MaterialSlot class and protocol

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type_name: str):
        self.__type = utils.validate_string(type_name)

    @property
    def data(self) -> BlenderMeshProtocol | None:
        return self.__data

    @data.setter
    def data(self, data: BlenderMeshProtocol | None):
        self.__data = data

    @property
    def modifiers(self) -> list:
        return self.__modifiers

    @property
    def material_slots(self) -> list[str | int]:
        return self.__material_slots

    @property
    def dict(self) -> dict[str, Any]:
        data: str | None = (None if self.type == "EMPTY" else self.data.name)
        return {
            self.name: {
                "type": self.type,
                "data": data,
                "modifiers": self.modifiers,
                "material_slots": self.material_slots
            }
        }

    def init_from_object(self, obj: BlenderObjectProtocol):
        self.name = obj.name
        self.type = obj.type
        self.data = obj.data


def blender_object_generator(objects: Iterable) -> Generator[BlenderObject, None, None]:
    for obj in objects:
        blender_object: BlenderObject = BlenderObject()
        blender_object.init_from_object(obj)
        yield blender_object
