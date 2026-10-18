
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.parent_child import ParentChild


class ParentChildRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_links_for_child(
        self,
        child_id: UUID,
    ) -> list[ParentChild]:
        return (
            self.db.query(ParentChild)
            .filter(ParentChild.child_id == child_id)
            .all()
        )

    def get_link(
        self,
        parent_id: UUID,
        child_id: UUID,
    ) -> ParentChild | None:
        return (
            self.db.query(ParentChild)
            .filter(
                ParentChild.parent_id == parent_id,
                ParentChild.child_id == child_id,
            )
            .first()
        )

    def create(self, link: ParentChild) -> ParentChild:
        self.db.add(link)
        self.db.flush()
        return link
