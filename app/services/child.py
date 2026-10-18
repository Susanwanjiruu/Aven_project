
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.child import Child
from app.repositories.child import ChildRepository


class ChildService:
    def __init__(self, db: Session):
        self.repository = ChildRepository(db)

    def get_child(self, child_id: UUID) -> Child | None:
        return self.repository.get_by_id(child_id)

    def list_children(self) -> list[Child]:
        return self.repository.list_all()
