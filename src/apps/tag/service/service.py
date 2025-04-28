from src.shared.depeneds import ITagRepository
from src.apps.tag.domain import TagEntity


class TagsService:
    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def create_tag(self, tag: TagEntity):
        tag = self.repository.create(tag)
        return tag
