from repositories import user_repository
from schemas.User import UserCreate, UserResponse
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    return user_repository.create_user(db, user)

def get_user(db: Session, user_id: int):
    return user_repository.get_user(db, user_id)

def get_all_users(db: Session):
    return user_repository.get_all_users(db)

def update_user(db: Session, user_id: int, user: UserCreate):
    return user_repository.update_user(db, user_id, user)

def delete_user(db: Session, user_id: int):
    return user_repository.delete_user(db, user_id)