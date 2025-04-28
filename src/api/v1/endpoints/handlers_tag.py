from fastapi import APIRouter, Body

from src.apps.tag.mappers import TagMapper
from src.apps.tag.service.service import TagsService
from src.apps.tag.infrastructure import TagRepository
from src.shared.dtos import TagDTO
from src.config.database.session import ISession

router = APIRouter(tags=['Tags'])


@router.post("/tag/create")
def create_tag(session: ISession, tag: str = Body(embed=True)):
    dto = TagDTO(tag=tag)
    tag_entity = TagMapper.dto_to_entity(dto=dto)

    # вот здесь создаём репозиторий
    repository = TagRepository(session)

    # а сюда уже его передаём
    tag_service = TagsService(repository)

    res = tag_service.create_tag(tag_entity)

    return {"result": res}
