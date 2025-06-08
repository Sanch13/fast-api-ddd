from typing import AsyncIterable

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.exc import SQLAlchemyError

from dishka import Provider, Scope, provide

from src_dishka.apps.tag.infrastructure.tag_repository import TagRepository
from src_dishka.apps.tag.interactors.create_tag_interactor import TagCreateInteractor
from src_dishka.apps.tag.interactors.get_all_tags_interactor import GetAllTagsInteractor
from src_dishka.apps.tag.interactors.get_tag_by_id_interactor import GetTagByIdInteractor
from src_dishka.apps.tag.repository import ITagRepository


class AsyncDatabaseHelperProvider(Provider):
    """"
    Класс для асинхронной работы с базой данных
    """

    @provide(scope=Scope.APP)
    def provide_async_engine(self) -> AsyncEngine:
        return create_async_engine(url="sqlite+aiosqlite:///fast-api.db", echo=True, future=True)

    @provide(scope=Scope.APP)
    def provide_async_session(self, async_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=async_engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def get_session(self, async_session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        """Создаёт сессию и автоматически закрывает её после использования"""
        async with async_session_maker() as session:
            try:
                yield session
            except SQLAlchemyError:
                await session.rollback()
                raise
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    tag_repository = provide(source=TagRepository, provides=ITagRepository)


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    create_tag = provide(source=TagCreateInteractor)
    all_tags = provide(source=GetAllTagsInteractor)
    get_tag_by_id = provide(source=GetTagByIdInteractor)
