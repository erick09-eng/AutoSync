from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.user_service import (
    create_user,
    get_user,
    get_all_users,
    update_user,
    delete_user,
)
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def read(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=list[UserResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user)

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
