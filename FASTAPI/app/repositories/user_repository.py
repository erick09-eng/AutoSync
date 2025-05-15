#app/repositories/user_repository.py
"""
    user_repository.py
    User Repository module.
    This module contains the data access layer for user-related operations.
    It interacts with the database to perform CRUD operations.
"""
from models.users import User
from schemas.UserSchema import UserCreate
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    """Create a new user."""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    """Get a user by its ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    """Get all users."""
    return db.query(User).all()

def update_user(db: Session, user_id: int, user: UserCreate):
    """Update an existing user."""
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()

def delete_user(db: Session, user_id: int):
    """Delete a user."""
    db_user = get_user(db, user_id)
