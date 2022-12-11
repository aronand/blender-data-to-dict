from typing import Any, Protocol, runtime_checkable

from .blendermeshprotocol import BlenderMeshProtocol


@runtime_checkable
class BlenderObjectProtocol(Protocol):
    """Defines/recreates an interface similar to bpy.types.Object"""
    @property
    def name(self) -> str: ...

    @property
    def type(self) -> str: ...

    @property
    def data(self) -> BlenderMeshProtocol | None: ...

    @property
    def modifiers(self) -> Any: ...  # TODO: What does modifiers actually return? -> bpy_prop_collection

    @property
    def material_slots(self) -> Any: ...  # TODO: What does material_slots actually return? -> bpy_prop_collection
