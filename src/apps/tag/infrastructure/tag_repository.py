from src.shared.dtos import TagDTOResponse
from src.apps.tag.infrastructure.models.tag import Tag
from src.apps.tag.domain import TagEntity
from src.apps.tag.repository import ITagRepository
from src.config.database.session import ISession
from src.apps.tag.mappers import TagMapper


class TagRepository(ITagRepository):
    model = Tag

    def __init__(self, db: ISession):
        self.db = db

    def create(self, tag: TagEntity) -> TagDTOResponse | None:
        instance = self.model(tag=tag.tag)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return TagMapper.model_to_dto(instance)

    def get_all(self):
        return self.db.query(Tag).all()

    def get_by_id(self, tag_id: int):
        return self.db.query(Tag).filter(Tag.id == tag_id).first()
