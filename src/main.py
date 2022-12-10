import bpy
from copy import deepcopy
from typing import Any, Iterable


class BlenderData:
    """Base class for all Blender data container classes."""
    __slots__ = ["__entries"]

    def __init__(self):
        self.__entries: dict[str, Any] = {}

    @property
    def entries(self) -> dict[str, Any]:
        return deepcopy(self.__entries)

    def __setitem__(self, key: str, value: Any):
        self.__entries[key] = value


class BlenderObjects(BlenderData):
    """Holds information about each object found in bpy.data.objects."""
    def __init__(self, objects: Iterable):
        super().__init__()
        self.__add_object_entries(objects)

    def __add_object_entries(self, objects: Iterable):
        for obj in objects:
            entry: dict[str, Any] = self.create_object_entry(obj)
            self[obj.name] = entry

    def create_object_entry(self, obj: bpy.types.Object) -> dict[str, Any]:
        return {
            "type": obj.type,
            "data": 0 if obj.data is None else obj.data.name,  # Used to point to the right data based on object type
            "modifiers": self.get_object_modifiers(obj),
            "materials": [material_slot.name for material_slot in obj.material_slots]
        }

    def get_object_modifiers(self, obj: bpy.types.Object) -> list[dict[str, Any]]:
        modifiers: list[dict[str, Any]] = []
        for modifier in obj.modifiers:
            modifiers.append({
                "type": modifier.type
            })
        return modifiers


def blender_data_to_dict() -> dict[str, Any]:
    objects: BlenderObjects = BlenderObjects(bpy.data.objects)
    return {
        "objects": objects.entries
    }


if __name__ == "__main__":
    data: dict[str, Any] = blender_data_to_dict()
    print(data)
