#app/schemas/category_schema.py
# pylint: disable=too-few-public-methods
"""Schema for managing categories in the database."""
from typing import Optional
from pydantic import BaseModel


# pylint: disable=too-few-public-methods
class CategoryBase(BaseModel):
    """Base schema for categories."""
    name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None


class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""

class CategoryUpdate(CategoryBase):
    """Schema for updating an existing category."""
    
    
class CategoryResponse(CategoryBase):
    """Schema for returning category data."""
    category_id: int

    class Config:
        """Configuration for the schema."""
        from_attributes = True
