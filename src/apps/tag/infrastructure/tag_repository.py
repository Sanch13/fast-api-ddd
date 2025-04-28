from src.shared.dtos import TagDTO
# from src.apps.tag.infrastructure import Tag
from .tag import Tag
from src.apps.tag.domain import TagEntity
from src.config.database.session import ISession


class TagRepository:
    model = Tag

    def __init__(self, db: ISession):
        self.db = db

    def create(self, tag: TagEntity):
        instance = self.model(tag=tag.tag)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return self._get_dto(instance)

    def _get_dto(self, row: Tag):
        return TagDTO(
            id=row.id,
            tag=row.tag,
        )
