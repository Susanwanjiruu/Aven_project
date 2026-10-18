
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.parent import Parent


class ParentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, parent_id: UUID) -> Parent | None:
        return (
            self.db.query(Parent)
            .filter(Parent.parent_id == parent_id)
            .first()
        )

    def get_by_email(self, email: str) -> Parent | None:
        return (
            self.db.query(Parent)
            .filter(Parent.email == email)
            .first()
        )

    def list_all(self) -> list[Parent]:
        return (
            self.db.query(Parent)
            .order_by(Parent.created_at.desc())
            .all()
        )

    def create(self, parent: Parent) -> Parent:
        self.db.add(parent)
        self.db.commit()
        self.db.refresh(parent)
        return parent

    def delete(self, parent: Parent) -> None:
        self.db.delete(parent)
        self.db.commit()
