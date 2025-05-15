#schemas/product_promotions.py
# pylint: disable=too-few-public-methods
"""Product promotions schema module.
This module defines the Pydantic models for product promotions.
"""
from pydantic import BaseModel

class ProductPromotionsBase(BaseModel):
    """Base model for product promotions."""
    product_id : int
    promotion_id : int
    
class ProductPromotionsCreate(ProductPromotionsBase):
    """Model for creating product promotions."""

class ProductPromotionsResponse(ProductPromotionsBase):
    """Model for product promotions response."""

    class Config:
        """Pydantic configuration."""
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models
