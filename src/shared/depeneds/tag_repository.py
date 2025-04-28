from typing import Annotated
from fastapi import Depends

from src.apps.tag.infrastructure import TagRepository


ITagRepository = Annotated[TagRepository, Depends()]
