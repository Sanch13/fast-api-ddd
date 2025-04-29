from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


class TagDTOInput(BaseModel):
    tag: str


@dataclass
class TagDTOResponse:
    id: int
    tag: str
    created_at: datetime
    updated_at: datetime
