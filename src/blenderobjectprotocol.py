from typing import Any, Protocol


class BlenderObjectProtocol(Protocol):
    @property
    def name(self) -> str: ...

    @property
    def type(self) -> str: ...

    @property
    def data(self) -> Any: ...  # TODO: Switch to BlenderMeshProtocol once implemented

    @property
    def modifiers(self) -> Any: ...  # TODO: What does modifiers actually return?

    @property
    def material_slots(self) -> Any: ...  # TODO: What does material_slots actually return?
