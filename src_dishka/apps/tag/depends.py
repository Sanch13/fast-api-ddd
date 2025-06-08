from typing import Annotated

from fastapi import Depends

from src_dishka.apps.tag.infrastructure.tag_repository import TagRepository
from src_dishka.config.database.session import ISession
from src_dishka.apps.tag.services.create_tag_service import TagCreateInteractor
from src_dishka.apps.tag.services.get_list_tags_service import GetAllTagsInteractor
from src_dishka.apps.tag.services.get_tag_by_id_service import GetTagByIdInteractor


class TagServiceDepends:
    @staticmethod
    def get_tag_create_service(db: ISession) -> TagCreateInteractor:
        return TagCreateInteractor(TagRepository(db=db))

    @staticmethod
    def get_all_tags_service(db: ISession) -> GetAllTagsInteractor:
        return GetAllTagsInteractor(TagRepository(db=db))

    @staticmethod
    def get_tag_by_id(db: ISession) -> GetTagByIdInteractor:
        return GetTagByIdInteractor(TagRepository(db=db))


ITagCreateService = Annotated[TagCreateInteractor, Depends(TagServiceDepends.get_tag_create_service)]
IGetAllTagsService = Annotated[GetAllTagsInteractor, Depends(TagServiceDepends.get_all_tags_service)]
IGetTagByIdService = Annotated[GetTagByIdInteractor, Depends(TagServiceDepends.get_tag_by_id)]
