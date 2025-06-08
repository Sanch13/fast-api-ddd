from abc import ABC, abstractmethod
from typing import Any


class BaseInteractor(ABC):
    """Базовый класс для сервисов."""

    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any: ...
