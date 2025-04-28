from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DatabaseHelper:
    """
    Класс для работы с базой данных
    """
    def __init__(self, database_url: str):
        self.engine = create_engine(
            url=database_url,
            connect_args={"check_same_thread": False}  # Нужно для SQLite
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_session(self) -> Session:
        """Создаёт сессию и автоматически закрывает её после использования"""
        session: Session = self.session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


DATABASE_URL = "sqlite:///fast-api.db"
db_helper = DatabaseHelper(database_url=DATABASE_URL)

