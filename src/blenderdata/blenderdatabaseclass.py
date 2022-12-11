from abc import ABC, abstractmethod
from typing import Any


class BlenderDataBaseClass(ABC):
    """Base class for all Blender data emulating classes"""
    @property
    @abstractmethod
    def dict(self) -> dict[str, Any]: pass
