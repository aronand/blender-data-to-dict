from typing import Any

from .blenderdatabaseclass import BlenderDataBaseClass


class BlenderMesh(BlenderDataBaseClass):
    def __init__(self):
        super().__init__()

    @property
    def dict(self) -> dict[str, Any]:
        return {self.name: {}}
