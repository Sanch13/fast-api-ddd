from pydantic import BaseModel


class TagDTO(BaseModel):
    tag: str
