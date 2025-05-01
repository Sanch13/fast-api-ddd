from typing import List

from fastapi import APIRouter, Body

from src.apps.tag.depends import ITagCreateService, IGetAllTagsService, IGetTagByIdService
from src.shared.dtos import TagDTOInput
from src.shared.models.tag import TagOut

router = APIRouter(tags=['Tags'])


@router.post("/tag/create", response_model=TagOut)
def create_tag(service: ITagCreateService, tag: str = Body(embed=True)):
    dto = TagDTOInput(tag=tag)
    # return asdict(service.execute(tag=dto.tag))
    return service.execute(tag=dto.tag)


@router.get("/tag/list", response_model=List[TagOut])
def list_tags(service: IGetAllTagsService):
    return service.execute()


@router.get("/tag/{tag_id}", response_model=TagOut)
def get_tag(service: IGetTagByIdService, tag_id: int):
    return service.execute(tag_id)
