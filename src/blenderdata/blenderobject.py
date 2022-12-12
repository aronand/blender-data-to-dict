from typing import Any

from . import utils
from .blenderdatabaseclass import BlenderDataBaseClass
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
