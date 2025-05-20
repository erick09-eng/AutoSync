"""
user_schema.py
This module defines the Pydantic models for the User entity.
It includes models for creating, updating, and retrieving users.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Base schema for User model.
    This schema is used for creating and updating users.
    It includes common fields such as username, password_hash, full_name,
    email, role_id, is_active, created_at, and updated_at.
    """
    username: str
    password_hash: str
    full_name: str
    email: Optional[EmailStr] = None
    role_id: int
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits from UserBase and includes additional validation if needed.
    """
    pass


class UserUpdate(UserBase):
    """
    Schema for updating an existing user.
    Inherits from UserBase and includes additional validation if needed.
    """
    pass


class UserResponse(UserBase):
    """
    Schema for retrieving a user.
    Inherits from UserBase and includes the user ID.
    """
    user_id: int

    class Config: # pylint: disable=too-few-public-methods
        from_attributes = True
