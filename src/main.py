from fastapi import FastAPI

from src.api.v1.endpoints.handlers_first import router as first_router
from src.api.v1.endpoints.handlers_tag import router as tag_router
from src.api.v1.endpoints.handlers_explorer import router as explorer_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Simple APP',
        docs_url='/api/docs',
        description='Simple DDD example',
        debug=True,
    )

    app.include_router(first_router)
    app.include_router(tag_router)
    app.include_router(explorer_router)

    return app
