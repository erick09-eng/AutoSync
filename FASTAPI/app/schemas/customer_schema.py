"""FastAPI schema for Sale model"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    """Base schema for Customer model"""
    tax_id: str
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CustomerCreate(CustomerBase):
    """Schema for creating new Customer records"""
    pass


class CustomerUpdate(CustomerBase):
    """Schema for updating existing Customer records"""
    pass


class CustomerResponse(CustomerBase):
    """Schema for Customer response including ID"""
    customer_id: int

    class Config: # pylint: disable=too-few-public-methods
        """Configuration for Pydantic models."""
        from_attributes = True
