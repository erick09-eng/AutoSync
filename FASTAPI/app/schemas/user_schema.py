"""
user_schema.py
This module defines the Pydantic models for the User entity.
It includes models for creating, updating, and retrieving users.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

# pylint: disable=too-few-public-methods
class UserBase(BaseModel):
    """
    Base schema for User model.
    This schema is used for creating and updating users.
    It includes common fields such as username, password_hash, full_name,
    email, role_id, is_active.
    """
    username: str
    password_hash: str
    full_name: str
    email: Optional[EmailStr] = None
    role_id: int
    is_active: Optional[bool] = True
    #  Note: created_at and updated_at are set automatically in the backend

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits from UserBase and includes additional validation if needed.
    """

class UserUpdate(BaseModel): # if use UserBase, it will not be partial,
    # but con baseModel it will be partial
    """Schema for updating an existing user."""
    # Inherits from UserBase and allows partial updates.
    username: Optional[str] = None
    password_hash: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None
    is_active: Optional[bool] = None
    # Note: created_at and updated_at are not included here as they are managed by the backend

class UserResponse(UserBase):
    """
    Schema for retrieving a user.
    Inherits from UserBase and includes the user ID.
    """
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration."""
        from_attributes = True
