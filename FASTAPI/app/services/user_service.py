#app/services/user_service.py
"""User service module.
This module contains the business logic for user-related operations.
It interacts with the user repository to perform CRUD operations.
"""
from repositories import user_repository
from schemas.user_schema import UserCreate
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    """Create a new user."""
    return user_repository.create_user(db, user)

def get_user(db: Session, user_id: int):
    """Get a user by its ID."""
    return user_repository.get_user(db, user_id)

def get_all_users(db: Session):
    """Get all users."""
    return user_repository.get_all_users(db)

def update_user(db: Session, user_id: int, user: UserCreate):
    """Update an existing user."""
    return user_repository.update_user(db, user_id, user)

def delete_user(db: Session, user_id: int):
    """Delete a user."""
    return user_repository.delete_user(db, user_id)