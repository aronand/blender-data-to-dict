from typing import Any

from . import utils


class BlenderDataBaseClass:
    """Base class for all Blender data emulating classes"""
    __slots__ = ["__name"]

    def __init__(self):
        self.__name: str = ""  # name should never be "", treat as error

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = utils.validate_string(name)

    @property
    def dict(self) -> dict[str, Any]: raise NotImplementedError
