
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from app.schemas.child import ChildResponse
from app.services.child import ChildService

router = APIRouter(prefix="/children", tags=["Children"])


@router.get("/", response_model=list[ChildResponse])
def list_children(db: Session = Depends(get_db)):
    return ChildService(db).list_children()
