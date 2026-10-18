
import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Parent(Base):
    __tablename__ = "parents"

    parent_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    full_name = Column(
        String(100),
        nullable=False,
    )
    email = Column(
        String(255),
        nullable=True,
        unique=True,
        index=True,
    )
    phone_number = Column(
        String(20),
        nullable=True,
    )
    phone_verified = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )
    whatsapp_opted_in = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )
    sms_opted_in = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )
    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    children = relationship(
        "ParentChild",
        back_populates="parent",
        cascade="all, delete-orphan",
    )
