from src_dishka.lib.base_model import Base
from pydantic import BaseModel


class Explorer(BaseModel):
    name: str
    country: str
    description: str
