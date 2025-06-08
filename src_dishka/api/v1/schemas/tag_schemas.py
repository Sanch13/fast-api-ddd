from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TagInputSchemas(BaseModel):
    tag: str


class TagOutputSchemas(BaseModel):
    id: int
    tag: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
