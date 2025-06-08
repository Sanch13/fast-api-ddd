from typing import List

from fastapi import APIRouter, Body, status

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute

from src_dishka.api.v1.schemas.tag_schemas import TagInputSchemas, TagOutputSchemas
from src_dishka.shared.dtos import TagDTOInput
from src_dishka.shared.models.tag import TagOut

from src_dishka.apps.tag.interactors.create_tag_interactor import TagCreateInteractor
from src_dishka.apps.tag.interactors.get_all_tags_interactor import GetAllTagsInteractor
from src_dishka.apps.tag.interactors.get_tag_by_id_interactor import GetTagByIdInteractor

router = APIRouter(route_class=DishkaRoute, tags=['Tags'])


@router.post("/tag", status_code=status.HTTP_201_CREATED, response_model=TagOutputSchemas)
async def create_tag(interactor: FromDishka[TagCreateInteractor], body: TagInputSchemas):
    tag_dto = TagDTOInput(**body.model_dump())
    return await interactor.execute(tag_dto=tag_dto)


@router.get("/tag/list", status_code=status.HTTP_200_OK, response_model=list[TagOutputSchemas])
async def get_all_tags(interactor: FromDishka[GetAllTagsInteractor]):
    tags_dto = await interactor.execute()
    return [TagOutputSchemas.model_validate(tag) for tag in tags_dto]


@router.get("/tag/{tag_id}", status_code=status.HTTP_200_OK, response_model=TagOutputSchemas)
async def get_tag(interactor: FromDishka[GetTagByIdInteractor], tag_id: int):
    tag = await interactor.execute(tag_id=tag_id)
    return TagOutputSchemas.model_validate(tag)
