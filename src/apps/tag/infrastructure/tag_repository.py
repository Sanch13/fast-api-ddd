from src.apps.tag.infrastructure.models.tag import Tag
from src.apps.tag.repository import ITagRepository
from src.config.database.session import ISession


class TagRepository(ITagRepository):
    model = Tag

    def __init__(self, db: ISession):
        self.db = db

    def create(self, tag: str):
        instance = self.model(tag=tag)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        # return TagMapper.model_to_dto(instance)
        return instance

    def get_all(self):
        return self.db.query(Tag).all()

    def get_by_id(self, tag_id: int):
        # instance = self.db.query(Tag).filter(Tag.id == tag_id).first()
        # return TagOut.model_validate(instance)
        return self.db.query(Tag).filter(Tag.id == tag_id).first()
