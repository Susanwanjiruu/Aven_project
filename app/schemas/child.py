
from datetime import datetime

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ChildCreate(BaseModel):
    display_name: str = Field(
        min_length=1,
        max_length=100,
    )
    parent_id: UUID


class ChildResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    child_id: UUID
    display_name: str
    is_active: bool
    created_at: datetime
