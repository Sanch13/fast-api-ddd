from abc import ABC, abstractmethod

from src.apps.tag.domain.tag_entity import TagEntity
from src.shared.dtos import TagDTOResponse


class ITagRepository(ABC):
    @abstractmethod
    def create(self, tag: str) -> TagDTOResponse | None:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get_by_id(self, tag_id: int):
        pass
