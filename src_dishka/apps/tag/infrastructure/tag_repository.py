from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select, select

from src_dishka.apps.tag.domain import TagEntity
from src_dishka.apps.tag.infrastructure.models.tag import Tag
from src_dishka.apps.tag.repository import ITagRepository
from src_dishka.apps.tag.mappers import TagMapper
from src_dishka.shared.dtos import TagDTOResponse


class TagRepository(ITagRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = Tag
        self.mapper = TagMapper()

    async def create(self, tag: TagEntity) -> TagDTOResponse:
        tag_model = self.mapper.entity_to_model(entity=tag)
        self.session.add(tag_model)
        await self.session.commit()
        await self.session.refresh(tag_model)
        return self.mapper.model_to_dto(tag_model)

    async def get_all_tags(self) -> list[TagEntity]:
        result = await self.session.execute(select(self.model))
        tag_models = result.scalars().all()
        return [self.mapper.model_to_entity(model) for model in tag_models]

    async def get_by_id(self, tag_id: int) -> TagEntity:
        query = select(self.model).filter_by(id=tag_id)
        result = await self.session.execute(query)
        tag_model = result.scalar_one_or_none()
        return self.mapper.model_to_entity(tag_model)
