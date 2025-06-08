from src_dishka.shared.service.base_service import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository


class GetTagByIdInteractor(BaseInteractor):
    """Service to get tag by id"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self, tag: int):
        return self.repository.get_by_id(tag)
