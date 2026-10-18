
import uuid

from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class ParentChild(Base):
    __tablename__ = "parent_children"

    __table_args__ = (
        UniqueConstraint(
            "parent_id",
            "child_id",
            name="uq_parent_child",
        ),
        CheckConstraint(
            "slot IN (1, 2)",
            name="ck_parent_child_slot",
        ),
        UniqueConstraint(
            "child_id",
            "slot",
            name="uq_child_parent_slot",
        ),
    )

    link_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    parent_id = Column(
        UUID(as_uuid=True),
        ForeignKey("parents.parent_id", ondelete="RESTRICT"),
        nullable=False,
    )
    child_id = Column(
        UUID(as_uuid=True),
        ForeignKey("children.child_id", ondelete="RESTRICT"),
        nullable=False,
    )
    slot = Column(
        Integer,
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    parent = relationship(
        "Parent",
        back_populates="children",
    )
    child = relationship(
        "Child",
        back_populates="parents",
    )
