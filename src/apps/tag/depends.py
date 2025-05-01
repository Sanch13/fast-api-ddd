from typing import Annotated

from fastapi import Depends

from src.apps.tag.infrastructure.tag_repository import TagRepository
from src.config.database.session import ISession
from src.apps.tag.services.create_tag_service import TagCreateService
from src.apps.tag.services.get_list_tags_service import GetAllTagsService
from src.apps.tag.services.get_tag_by_id_service import GetTagByIdService


class TagServiceDepends:
    @staticmethod
    def get_tag_create_service(db: ISession) -> TagCreateService:
        return TagCreateService(TagRepository(db=db))

    @staticmethod
    def get_all_tags_service(db: ISession) -> GetAllTagsService:
        return GetAllTagsService(TagRepository(db=db))

    @staticmethod
    def get_tag_by_id(db: ISession) -> GetTagByIdService:
        return GetTagByIdService(TagRepository(db=db))


ITagCreateService = Annotated[TagCreateService, Depends(TagServiceDepends.get_tag_create_service)]
IGetAllTagsService = Annotated[GetAllTagsService, Depends(TagServiceDepends.get_all_tags_service)]
IGetTagByIdService = Annotated[GetTagByIdService, Depends(TagServiceDepends.get_tag_by_id)]
