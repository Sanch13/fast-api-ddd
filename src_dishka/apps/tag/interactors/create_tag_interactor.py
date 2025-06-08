from src_dishka.shared.dtos import TagDTOInput
from src_dishka.shared.service.base_interactor import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository
from src_dishka.apps.tag.mappers import TagMapper


class TagCreateInteractor(BaseInteractor):
    """Service to create a new tag"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    async def execute(self, tag_dto: TagDTOInput):
        tag_entity = TagMapper.dto_to_entity(tag_dto)
        return await self.repository.create(tag_entity)
