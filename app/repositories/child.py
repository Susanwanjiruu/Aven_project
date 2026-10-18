
import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.models.child import Child


class ChildRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, child_id: uuid.UUID) -> Optional[Child]:
        return (
            self.db.query(Child)
            .filter(Child.child_id == child_id)
            .first()
        )

    def list_all(self) -> list[Child]:
        return (
            self.db.query(Child)
            .order_by(Child.created_at.desc())
            .all()
        )

    def create(self, child: Child) -> Child:
        self.db.add(child)
        self.db.commit()
        self.db.refresh(child)
        return child

    def update(self, child: Child) -> Child:
        self.db.commit()
        self.db.refresh(child)
        return child

    def delete(self, child: Child) -> None:
        self.db.delete(child)
        self.db.commit()
