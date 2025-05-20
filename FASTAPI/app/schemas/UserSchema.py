"""
    User Schema
    This module contains the Pydantic models for user data validation and serialization.
    It includes models for creating, updating, and responding with user data.
    The models are used in the API endpoints to ensure that the data received and sent
    is in the correct format.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base schema for user data."""
    username: str
    password_hash: str
    full_name: str
    email: Optional[EmailStr] = None
    role_id: int
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserCreate(UserBase):
    """Schema for creating a new user."""
    pass


class UserUpdate(UserBase):
    """Schema for updating an existing user."""
    pass


class UserResponse(UserBase):
    """Schema for responding with user data."""
    user_id: int

    class Config: # pylint: disable=too-few-public-methods
        from_attributes = True
