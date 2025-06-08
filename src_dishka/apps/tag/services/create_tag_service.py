from src_dishka.apps.tag.domain import TagEntity
from src_dishka.shared.service.base_interactor import BaseInteractor
from src_dishka.apps.tag.repository import ITagRepository


class TagCreateInteractor(BaseInteractor):
    """Service to create a new tag"""

    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def execute(self, tag: TagEntity):
        return self.repository.create(tag)
