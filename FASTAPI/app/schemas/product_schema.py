"""FastAPI schema for Sale model"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    """Base schema for Product model"""
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
    """Schema for creating new Product records"""
    pass


class ProductUpdate(ProductBase):
    """Schema for updating existing Product records"""
    pass


class ProductResponse(ProductBase):
    """Schema for Product response including ID"""
    product_id: int

    class Config: # pylint: disable=too-few-public-methods
        """Configuration for Pydantic models"""
        from_attributes = True
