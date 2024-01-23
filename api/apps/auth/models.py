from datetime import datetime
from typing import final

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import TIMESTAMP
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String

from api.database import Base

metadata = MetaData()


@final
class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=True, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


user_matadata = Base.metadata
