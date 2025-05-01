from src.shared.service.base_service import BaseService
from src.apps.tag.repository import ITagRepository


class GetAllTagsService(BaseService):
    """Service gets all tags"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
