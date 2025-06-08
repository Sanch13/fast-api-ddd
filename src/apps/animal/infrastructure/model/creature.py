from src_dishka.lib.base_model import Base
from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str
