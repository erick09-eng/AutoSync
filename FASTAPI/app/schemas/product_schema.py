#app/schemas/product_schema.py
# pylint: disable=too-few-public-methods
"""Product schema module.
This module defines the Pydantic models for product data.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class ProductBase(BaseModel):
    """
        Base model for product data.
    """
    sku: Optional[str] = None
    name: str
    description: Optional[str]
    category_id: int
    unit_price: float
    cost_price: Optional[float]
    current_stock: int
    min_stock: int
    on_offer: Optional[bool] = False
    offer_price: Optional[float] = None
    is_active: Optional[bool] = True
    #  Note: created_at and updated_at are set automatically in the backend

class ProductCreate(ProductBase):
    """
        Model for creating product data.
    """

class ProductUpdate(BaseModel):
    """
        Model for updating product data.
    """
    sku: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    unit_price: Optional[float] = None
    cost_price: Optional[float] = None
    current_stock: Optional[int] = None
    min_stock: Optional[int] = None
    on_offer: Optional[bool] = None
    offer_price: Optional[float] = None
    is_active: Optional[bool] = None
    # Note: created_at and updated_at are not included here as they are managed by the backend

class ProductResponse(ProductBase):
    """
        Model for product data response.
    """
    product_id: int
    create_at: datetime
    updated_at: datetime
    # Note: created_at and updated_at are not included here as they are managed by the backend

    class Config:
        """Pydantic configuration."""
        from_attributes = True
