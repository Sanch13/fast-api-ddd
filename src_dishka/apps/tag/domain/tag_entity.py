from dataclasses import dataclass
from datetime import datetime


@dataclass
class TagEntity:
    tag: str
    id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
