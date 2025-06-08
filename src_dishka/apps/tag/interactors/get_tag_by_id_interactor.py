from src_dishka.shared.dtos import TagDTOInput, TagDTOResponse
from src_dishka.shared.service.base_interactor import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository
from src_dishka.apps.tag.mappers import TagMapper


class GetTagByIdInteractor(BaseInteractor):
    """Service to create a new tag"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    async def execute(self, tag_id: int) -> TagDTOResponse:
        tag_entity = await self.repository.get_by_id(tag_id)
        return TagMapper.entity_to_dto(tag_entity)
