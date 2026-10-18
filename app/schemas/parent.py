
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ParentCreate(BaseModel):
    full_name: str = Field(
        min_length=1,
        max_length=100,
    )
    email: EmailStr | None = None
    phone_number: str | None = Field(
        default=None,
        max_length=20,
    )
    whatsapp_opted_in: bool = False
    sms_opted_in: bool = False


class ParentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    parent_id: UUID
    full_name: str
    email: EmailStr | None
    phone_number: str | None
    phone_verified: bool
    whatsapp_opted_in: bool
    sms_opted_in: bool
    is_active: bool
    created_at: datetime
