import enum
import uuid

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    ForeignKeyConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class JourneyDirection(str, enum.Enum):
    home_to_school = "home_to_school"
    school_to_home = "school_to_home"


class JourneyStatus(str, enum.Enum):
    scheduled = "scheduled"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class Journey(Base):
    __tablename__ = "journeys"

    __table_args__ = (
        ForeignKeyConstraint(
            ["device_id", "child_id"],
            ["devices.device_id", "devices.child_id"],
            name="fk_journeys_device_child",
        ),
    )

    journey_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    child_id = Column(
        UUID(as_uuid=True),
        ForeignKey("children.child_id"),
        nullable=False,
    )
    device_id = Column(
        UUID(as_uuid=True),
        nullable=False,
    )
    direction = Column(
        Enum(JourneyDirection),
        nullable=False,
    )
    status = Column(
        Enum(JourneyStatus),
        nullable=False,
        default=JourneyStatus.scheduled,
    )
    planned_start_at = Column(
        DateTime(timezone=True),
        nullable=False,
    )
    actual_start_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )
    actual_end_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    child = relationship("Child", back_populates="journeys")
    device = relationship(
        "Device",
        foreign_keys=[device_id],
        viewonly=True,
    )
    telemetry_readings = relationship("Telemetry", back_populates="journey")
    events = relationship("Event", back_populates="journey")
