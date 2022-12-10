from abc import ABC, abstractmethod
from typing import Any


class BlenderData(ABC):
    @property
    @abstractmethod
    def dict(self) -> dict[str, Any]: pass
