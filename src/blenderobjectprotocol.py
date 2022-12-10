from typing import Any, Protocol


class BlenderObjectProtocol(Protocol):
    """Defines/recreates an interface similar to bpy.types.Object"""
    @property
    def name(self) -> str: ...

    @property
    def type(self) -> str: ...

    @property
    def data(self) -> Any: ...  # TODO: Switch to BlenderMeshProtocol once implemented

    @property
    def modifiers(self) -> Any: ...  # TODO: What does modifiers actually return? -> bpy_prop_collection

    @property
    def material_slots(self) -> Any: ...  # TODO: What does material_slots actually return? -> bpy_prop_collection
