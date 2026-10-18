
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.child import Child
from app.models.parent import Parent
from app.models.parent_child import ParentChild
from app.repositories.parent import ParentRepository
from app.schemas.registration import AdminRegistrationCreate


class RegistrationService:
    def __init__(self, db: Session):
        self.db = db
        self.parent_repository = ParentRepository(db)

    def register_parent_with_child(
        self, data: AdminRegistrationCreate
    ) -> tuple[Parent, Child]:
        full_name = data.parent.full_name.strip()
        display_name = data.child.display_name.strip()

        if not full_name:
            raise ValueError("Parent name cannot be empty.")

        if not display_name:
            raise ValueError("Child name cannot be empty.")

        email = (
            str(data.parent.email).strip().lower()
            if data.parent.email
            else None
        )
        phone_number = (
            data.parent.phone_number.strip()
            if data.parent.phone_number
            else None
        )

        if (
            data.parent.whatsapp_opted_in
            or data.parent.sms_opted_in
        ) and not phone_number:
            raise ValueError(
                "A phone number is required for notifications."
            )

        if email and self.parent_repository.get_by_email(email):
            raise ValueError(
                "A parent with this email already exists."
            )

        parent = Parent(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            phone_verified=False,
            whatsapp_opted_in=data.parent.whatsapp_opted_in,
            sms_opted_in=data.parent.sms_opted_in,
        )

        child = Child(display_name=display_name)

        try:
            self.db.add_all([parent, child])
            self.db.flush()

            link = ParentChild(
                parent_id=parent.parent_id,
                child_id=child.child_id,
                slot=1,
            )
            self.db.add(link)

            self.db.commit()
            self.db.refresh(parent)
            self.db.refresh(child)

            return parent, child

        except IntegrityError as exc:
            self.db.rollback()
            raise ValueError(
                "Registration failed. Check whether the parent's "
                "email is already registered."
            ) from exc

        except Exception:
            self.db.rollback()
            raise
