import uuid

from sqlalchemy import Column, DateTime, Float, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    telemetry_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    device_id = Column(
        UUID(as_uuid=True),
        ForeignKey("devices.device_id"),
        nullable=False,
    )
    journey_id = Column(
        UUID(as_uuid=True),
        ForeignKey("journeys.journey_id"),
        nullable=True,
    )
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    recorded_at = Column(DateTime(timezone=True), nullable=False)
    gps_accuracy = Column(Float, nullable=True)
    received_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    device = relationship("Device")
    journey = relationship("Journey", back_populates="telemetry_readings")
