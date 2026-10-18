
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import get_db
from app.core.security import get_current_admin
from app.schemas.registration import (
    AdminRegistrationCreate,
    AdminRegistrationResponse,
)
from app.services.registration import RegistrationService

router = APIRouter(
    prefix="/admin/registrations",
    tags=["Admin Registration"],
)


@router.post(
    "/",
    response_model=AdminRegistrationResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_parent_with_child(
    data: AdminRegistrationCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    try:
        parent, child = RegistrationService(
            db
        ).register_parent_with_child(data)

        return {
            "parent": parent,
            "child": child,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not complete registration.",
        ) from exc
