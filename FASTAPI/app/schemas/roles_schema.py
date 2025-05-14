"""
Role Schema Module

Defines Pydantic schemas for role data validation and serialization.
"""
from typing import Optional
from pydantic import BaseModel


class RoleBase(BaseModel):
    """
    Base schema for Role with common attributes.
    """
    role_name: str
    role_description: Optional[str] = None


class RoleCreate(RoleBase):
    """
    Schema for creating new roles (inherits from RoleBase).
    """
    pass


class RoleUpdate(RoleBase):
    """
    Schema for updating existing roles (inherits from RoleBase).
    """
    pass


class RoleResponse(RoleBase):
    """
    Complete Role schema including ID (for response models).
    """
    role_id: int


class Config: # pylint: disable=too-few-public-methods
    """Configuration for Pydantic models.
    Enables attribute-based access to model fields.
    """
    from_attributes = True
