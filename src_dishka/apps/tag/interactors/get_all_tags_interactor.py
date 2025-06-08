from src_dishka.shared.dtos import TagDTOInput, TagDTOResponse
from src_dishka.shared.service.base_interactor import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository
from src_dishka.apps.tag.mappers import TagMapper


class GetAllTagsInteractor(BaseInteractor):
    """Service to create a new tag"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    async def execute(self) -> list[TagDTOResponse]:
        tags_entity = await self.repository.get_all_tags()
        return [TagMapper.entity_to_dto(entity) for entity in tags_entity]
