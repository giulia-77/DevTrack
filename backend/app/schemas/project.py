
from pydantic import BaseModel, Field, ConfigDict


class ProjectCreate(BaseModel):
    UserID: int
    Title: str = Field(min_length=1, max_length=150)
    Description: str | None = None
    Technology: str | None = Field(default=None, max_length=100)
    Status: str = "planned"


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ProjectID: int
    UserID: int
    Title: str
    Description: str | None
    Technology: str | None
    Status: str
