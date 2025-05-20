#app/schemas/roles_schema.py
# pylint: disable=too-few-public-methods
"""Pydantic schemas for roles."""
from typing import Optional
from pydantic import BaseModel

class RoleBase(BaseModel):
    """Base schema for roles."""
    role_name: str
    role_description: Optional[str] = None

class RoleCreate(RoleBase):
    """Schema for creating a role."""

class RoleUpdate(RoleBase):
    """Schema for updating a role."""

class RoleResponse(RoleBase):
    """Schema for role response."""
    role_id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True
