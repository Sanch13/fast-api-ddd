from typing import List

from fastapi import APIRouter, Body

from src.apps.tag.mappers import TagMapper
from src.apps.tag.service.service import TagsService
from src.apps.tag.infrastructure.tag_repository import TagRepository
from src.shared.dtos import TagDTOInput, TagDTOResponse
from src.shared.models.tag import TagOut
from src.config.database.session import ISession

router = APIRouter(tags=['Tags'])


@router.post("/tag/create")
def create_tag(session: ISession, tag: str = Body(embed=True)):
    dto = TagDTOInput(tag=tag)
    tag_entity = TagMapper.dto_to_entity(dto=dto)
    return TagsService(TagRepository(session)).create_tag(tag_entity)


@router.get("/tag/list", response_model=List[TagOut])
def list_tags(session: ISession):
    # вот здесь создаём репозиторий
    repository = TagRepository(session)
    tag_service = TagsService(repository)
    res = tag_service.get_all_tags()
    return res


@router.get("/tag/{tag_id}", response_model=TagOut)
def get_tag(session: ISession, tag_id: int):
    repository = TagRepository(session)
    tag_service = TagsService(repository)
    return tag_service.get_tag(tag_id)

