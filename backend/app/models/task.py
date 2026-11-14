from sqlalchemy import Column, Integer, String, ForeignKey, Date

from backend.app.core.database import Base


class Task(Base):
    __tablename__ = "Tasks"

    TaskID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    ProjectID = Column(Integer, ForeignKey("Projects.ProjectID"), nullable=True)
    Title = Column(String(150), nullable=False)
    Priority = Column(Integer, default=1, nullable=False)
    Status = Column(String(30), default="pending")
    Deadline = Column(Date, nullable=True)
