from dataclasses import asdict

from src.apps.tag.repository import ITagRepository
from src.apps.tag.domain import TagEntity


class TagsService:
    def __init__(self, repository: ITagRepository):
        self.repository = repository

    def create_tag(self, tag: TagEntity) -> dict:
        tag_dto = self.repository.create(tag)
        return asdict(tag_dto)

    def get_all_tags(self):
        return self.repository.get_all()

    def get_tag(self, tag_id):
        return self.repository.get_by_id(tag_id)
