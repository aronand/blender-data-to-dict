from typing import Protocol, runtime_checkable


@runtime_checkable
class BlenderMeshProtocol(Protocol):
    """Defines/recreates an interface similar to bpy.types.Mesh"""
    @property
    def name(self) -> str: ...
