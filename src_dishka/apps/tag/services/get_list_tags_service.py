from src_dishka.shared.service.base_service import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository


class GetAllTagsInteractor(BaseInteractor):
    """Service gets all tags"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
