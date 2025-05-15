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
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ProductCreate(ProductBase):
    """
        Model for creating product data.
    """

class ProductUpdate(ProductBase):
    """
        Model for updating product data.
    """

class ProductResponse(ProductBase):
    """
        Model for product data response.
    """
    product_id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True
