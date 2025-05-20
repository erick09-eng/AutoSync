#app/schemas/customer_schema.py
"""Customer schema for FastAPI application.
This module contains the Pydantic models for customer data validation and serialization.
It includes models for creating, updating, and responding with customer data.
The models are used in the API endpoints to ensure that the data received and sent
is in the correct format.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    """Base schema for customer data."""
    tax_id: str
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CustomerCreate(CustomerBase):
    """Schema for creating a new customer."""

class CustomerUpdate(CustomerBase):
    """Schema for updating an existing customer."""

class CustomerResponse(CustomerBase):
    """Schema for responding with customer data."""
    customer_id: int

    class Config:
        """Configuration for Pydantic models."""
        from_attributes = True
