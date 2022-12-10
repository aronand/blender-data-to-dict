from typing import Any

import utils
from blenderdata import BlenderData
from blenderobjectprotocol import BlenderObjectProtocol


class BlenderObject(BlenderData):
    """Imitates bpy.types.Object. Compliant with BlenderObjectProtocol."""
    __slots__ = "__name", "__type", "__data", "__modifiers", "__material_slots"

    def __init__(self):
        self.__name: str = ""  # name should never be "", treat as error
        self.__type: str = ""  # type should never be "", treat as error
        self.__data: str | int = 0  # if int, treat as None, or error if type != "EMPTY"
        self.__modifiers: list = []  # TODO: Modifier class and protocol
        self.__material_slots: list = []  # TODO: MaterialSlot class and protocol

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = utils.validate_string(name)

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type_name: str):
        self.__type = utils.validate_string(type_name)

    @property
    def data(self) -> str | int:
        return self.__data

    @property
    def modifiers(self) -> list:
        return self.__modifiers

    @property
    def material_slots(self) -> list[str | int]:
        return self.__material_slots

    @property
    def dict(self) -> dict[str, Any]:
        return {
            self.name: {
                "type": self.type,
                "data": self.data,
                "modifiers": self.modifiers,
                "material_slots": self.material_slots
            }
        }

    def init_from_object(self, obj: BlenderObjectProtocol):
        self.name = obj.name
        self.type = obj.type
