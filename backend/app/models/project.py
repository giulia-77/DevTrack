from sqlalchemy import Column, Integer, String, ForeignKey, Text

from backend.app.core.database import Base


class Project(Base):
    __tablename__ = "Projects"

    ProjectID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    Title = Column(String(150), nullable=False)
    Description = Column(Text, nullable=True)
    Technology = Column(String(100), nullable=True)
    Status = Column(String(30), default="planned")
