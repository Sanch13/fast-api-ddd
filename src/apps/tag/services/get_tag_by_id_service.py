from src.shared.service.base_service import BaseService
from src.apps.tag.repository import ITagRepository


class GetTagByIdService(BaseService):
    """Service to get tag by id"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self, tag: int):
        return self.repository.get_by_id(tag)
