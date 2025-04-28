from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.config.database.engine import db_helper

ISession = Annotated[Session, Depends(db_helper.get_session)]
