import bpy
from copy import deepcopy
from typing import Any


class BlenderData:
    __slots__ = ["__entries"]

    def __init__(self):
        self.__entries: dict[str, Any] = {}

    @property
    def entries(self) -> dict[str, Any]:
        return deepcopy(self.__entries)

    def __setitem__(self, key: str, value: Any):
        self.__entries[key] = value


if __name__ == "__main__":
    pass
