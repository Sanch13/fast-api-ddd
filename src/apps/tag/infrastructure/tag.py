from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.lib.base_model import Base


class Tag(Base):
    """ Модель Tag

    :param id: идентификатор
    :param tag: название тега
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__: str = "tag"

    tag: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )
