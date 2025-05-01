from src.shared.service.base_service import BaseService
from src.apps.tag.repository import ITagRepository


class TagCreateService(BaseService):
    """Service to create a new tag"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self, tag: str):
        return self.repository.create(tag)
