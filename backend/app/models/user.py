from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.app.core.database import Base


class User(Base):
    __tablename__ = "Users"

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(50), nullable=False, unique=True)
    Email = Column(String(255), nullable=False, unique=True)
    CreatedAt = Column(DateTime, server_default=func.sysdatetime())
