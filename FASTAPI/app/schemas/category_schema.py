"""FastAPI schema for Sale model"""
from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    """Base schema for Category model"""
    name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None


class CategoryCreate(CategoryBase):
    """Schema for creating new Category records"""
    pass


class CategoryUpdate(CategoryBase):
    """Schema for updating existing Category records"""
    pass


class CategoryResponse(CategoryBase):
    """Schema for Category response including ID"""
    category_id: int

    class Config: # pylint: disable=too-few-public-methods
        """Configuration for Pydantic models"""
        from_attributes = True
