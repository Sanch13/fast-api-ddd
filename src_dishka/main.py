from fastapi import FastAPI

from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka

from src_dishka.api.v1.endpoints.handlers_first import router as first_router
from src_dishka.api.v1.endpoints.handlers_tag import router as tag_router
from src_dishka.providers.adapters import AsyncDatabaseHelperProvider, RepositoriesProvider, InteractorsProvider


def container_factory() -> AsyncContainer:
    return make_async_container(
        AsyncDatabaseHelperProvider(),
        RepositoriesProvider(),
        InteractorsProvider(),
    )


def init_di(app: FastAPI) -> None:
    container = container_factory()
    setup_dishka(container, app)


def create_app() -> FastAPI:
    app = FastAPI(
        title='Simple APP',
        docs_url='/api/docs',
        description='Simple DDD example',
        debug=True,
    )

    init_di(app)
    app.include_router(first_router)
    app.include_router(tag_router)

    return app
