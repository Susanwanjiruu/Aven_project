
from pydantic import BaseModel

from app.schemas.parent import ParentCreate, ParentResponse
from app.schemas.child import ChildResponse
from pydantic import Field


class ChildRegistrationDetails(BaseModel):
    display_name: str = Field(min_length=1, max_length=100)


class AdminRegistrationCreate(BaseModel):
    parent: ParentCreate
    child: ChildRegistrationDetails


class AdminRegistrationResponse(BaseModel):
    parent: ParentResponse
    child: ChildResponse
