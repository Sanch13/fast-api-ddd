from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    """Базовый класс для сервисов."""

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any: ...
