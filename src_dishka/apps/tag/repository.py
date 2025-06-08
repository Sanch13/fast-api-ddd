from abc import ABC, abstractmethod

from src_dishka.apps.tag.domain.tag_entity import TagEntity
from src_dishka.shared.dtos import TagDTOResponse


class ITagRepository(ABC):
    @abstractmethod
    async def create(self, tag: TagEntity) -> TagDTOResponse | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all_tags(self) -> list:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, tag_id: int):
        raise NotImplementedError
