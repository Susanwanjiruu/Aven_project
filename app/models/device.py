import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Device(Base):
    __tablename__ = "devices"

    __table_args__ = (
        UniqueConstraint(
            "device_id",
            "child_id",
            name="uq_devices_device_child",
        ),
    )

    device_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    child_id = Column(
        UUID(as_uuid=True),
        ForeignKey("children.child_id"),
        nullable=False,
    )
    device_code = Column(
        String(50),
        unique=True,
        nullable=False,
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

    child = relationship("Child", back_populates="devices")
