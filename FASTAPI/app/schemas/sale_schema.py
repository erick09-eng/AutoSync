#app/repositories/sales_repository.py
# pylint: disable=too-few-public-methods
"""
    Sale Schema
    This module contains the Pydantic models for sale data validation and serialization.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SaleBase(BaseModel):
    """
    Base model for sale data.
    """
    document_type_id: int
    serial_number: str
    customer_id: int
    user_id: int
    subtotal: float
    tax_amount: float
    discount_amount: Optional[float] = 0.0
    total_amount: Optional[float] = 0.0
    payment_method: int
    status: Optional[str] = "completed"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class SaleCreate(SaleBase):
    """
    Model for creating sale data.
    """


class SaleUpdate(SaleBase):
    """
    Model for updating sale data.
    """


class SaleResponse(SaleBase):
    """
    Model for sale data response.
    """
    sale_id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True
