#app/repositories/user_repository.py
"""
    user_repository.py
    User Repository module.
    This module contains the data access layer for user-related operations.
    It interacts with the database to perform CRUD operations.
"""
from datetime import datetime, timezone, timedelta

from models.users import User
from models.roles import Roles
from schemas.user_schema import UserCreate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_colombia_time():
    """Get current time in Colombia timezone (UTC-5)."""
    colombia_tz = timezone(timedelta(hours=-5))
    return datetime.now(colombia_tz)

def create_user(db: Session, user: UserCreate):
    """Create a new user."""

    # Validate the role_id exists in the database
    role = db.query(Roles).filter(Roles.role_id == user.role_id).first()
    if not role:
        raise HTTPException(
        status_code=404,
        detail=f"Role with id {user.role_id} not found"
        )

    # create dictionary for user data and add timestamps
    user_data = user.dict()
    user_data['created_at'] = get_colombia_time()
    user_data['updated_at'] = get_colombia_time()

    # create the user
    try:
        db_user = User(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(
                status_code=500,
                detail=f"An error occurred while creating the user: {str(e)}"
        ) from e

def get_user(db: Session, user_id: int):
    """Get a user by its ID."""
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        if not user.created_at:
            user.created_at = get_colombia_time()
        if not user.updated_at:
            user.updated_at = get_colombia_time()
    return user

def get_all_users(db: Session):
    """Get all users."""
    users = db.query(User).all()
    for user in users:
        if not user.created_at:
            user.created_at = get_colombia_time()
        if not user.updated_at:
            user.updated_at = get_colombia_time()

    return users

def update_user(db: Session, user_id: int, user: UserCreate):
    """Update an existing user."""
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )

    # update fields sending from the frontend
    update_data = user.dict(exclude_unset=True)
    update_data['updated_at'] = get_colombia_time()

    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)  # refresh the instance to get the updated values
    return db_user  # return the updated instance

def delete_user(db: Session, user_id: int):
    """Delete a user."""
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )
    db.delete(db_user)
    db.commit()
    return {
        "message": f"User with id {user_id} deleted successfully",
        "id": user_id
    }
