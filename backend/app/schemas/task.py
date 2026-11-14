
from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):
    UserID: int
    ProjectID: int | None = None
    Title: str = Field(min_length=1, max_length=150)
    Priority: int = Field(default=1, ge=1, le=5)
    Status: str = "pending"
    Deadline: date | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    TaskID: int
    UserID: int
    ProjectID: int | None
    Title: str
    Priority: int
    Status: str
    Deadline: date | None
