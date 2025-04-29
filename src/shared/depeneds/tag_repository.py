from typing import Annotated
from fastapi import Depends

from src.apps.tag.infrastructure.tag_repository import TagRepository


ITagRepository = Annotated[TagRepository, Depends()]
