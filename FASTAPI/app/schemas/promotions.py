#schemas/promotions.py
# pylint: disable=too-few-public-methods
"""Promotions schema module.
This module defines the Pydantic models for promotions data.
"""
from datetime import datetime
from pydantic import BaseModel

class PromotionsBase(BaseModel):
    """
        Base model for promotions data.
    """
    name : str
    description : str
    discount_type : str
    discount_value : float
    start_date : datetime
    end_date : datetime
    is_active : bool
    created_at : datetime

class PromotionsCreate(PromotionsBase):
    """ 
        Model for creating promotions data.
    """

class PromotionsResponse(PromotionsBase):
    """
        Model for promotions data response.
    """
    promotion_id : int

    class Config:
        """Pydantic configuration."""
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models
