"""FastAPI schema for Sale model"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SaleBase(BaseModel):
    """Base schema for Sale model"""
    document_type_id: int
    serial_number: str
    customer_id: int
    user_id: int
    subtotal: float
    tax_amount: float
    discount_amount: Optional[float] = 0.0
    total_amount: Optional[float] = 0.0
    payment_method: Optional[str] = "cash"
    status: Optional[str] = "completed"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class SaleCreate(SaleBase):
    """Schema for creating new Sale records"""
    pass


class SaleUpdate(SaleBase):
    """Schema for updating existing Sale records"""
    pass


class SaleResponse(SaleBase):
    """Schema for Sale response including ID"""
    sale_id: int

    class Config: # pylint: disable=too-few-public-methods
        """Configuration for Pydantic models"""
        from_attributes = True
