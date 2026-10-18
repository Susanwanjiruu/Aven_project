
import uuid

from sqlalchemy import Boolean, Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Child(Base):
    __tablename__ = "children"

    child_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    display_name = Column(
        String(100),
        nullable=False,
    )
    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    devices = relationship("Device", back_populates="child")
    geofences = relationship("Geofence", back_populates="child")
    journeys = relationship("Journey", back_populates="child")

    parents = relationship(
        "ParentChild",
        back_populates="child",
        cascade="all, delete-orphan",
    )
