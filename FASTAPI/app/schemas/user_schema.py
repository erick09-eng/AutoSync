"""""
User schema for FastAPI application.
This module defines the Pydantic models for user-related operations.
"""""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Base schema for User with common attributes.
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
    Schema for new user registration.

    Inherits all fields from UserBase.
    Additional validation can be added here for creation-specific rules.
    """
    pass


class UserUpdate(UserBase):
    """
    Schema for updating existing user information.

    Inherits all fields from UserBase.
    Additional validation can be added here for update-specific rules.
    """
    pass


class UserResponse(UserBase):
    """
    Complete user schema for API responses.

    Attributes:
        user_id (int): Unique database identifier
    """
    user_id: int

    class Config: # pylint: disable=too-few-public-methods
        from_attributes = True
