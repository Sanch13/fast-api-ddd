from dataclasses import dataclass
from datetime import datetime


@dataclass
class TagDTOInput:
    tag: str


@dataclass
class TagDTOResponse:
    id: int
    tag: str
    created_at: datetime
    updated_at: datetime
