import enum
import uuid

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class EventType(str, enum.Enum):
    route_deviation = "route_deviation"
    unusual_stop = "unusual_stop"
    abnormal_speed = "abnormal_speed"
    unexpected_delay = "unexpected_delay"
    gps_signal_lost = "gps_signal_lost"


class EventStatus(str, enum.Enum):
    pending = "pending"
    reviewed = "reviewed"
    dismissed = "dismissed"
    resolved = "resolved"


class Event(Base):
    __tablename__ = "events"

    event_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    journey_id = Column(
        UUID(as_uuid=True),
        ForeignKey("journeys.journey_id"),
        nullable=False,
    )
    event_type = Column(
        Enum(EventType),
        nullable=False,
    )
    status = Column(
        Enum(EventStatus),
        nullable=False,
        default=EventStatus.pending,
    )
    description = Column(Text, nullable=False)
    detected_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    reviewed_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    journey = relationship("Journey", back_populates="events")
