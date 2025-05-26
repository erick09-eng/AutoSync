#app/schemas/payments.py
"""Payments schema module.
This module contains the Pydantic schemas for payments.
Classes:
    PaymentBase: Base schema for payments.
    PaymentCreate: Schema for creating a payment.
    PaymentResponse: Schema for response of payment.
"""
# pylint: disable=too-few-public-methods
from datetime import datetime
from pydantic import BaseModel

class PaymentBase(BaseModel):
    """Base schema for payments"""
    sale_id : int
    payment_method_id : int
    amount : float
    transaction_code : str
    payment_date : datetime
    status : str

class PaymentCreate(PaymentBase):
    """Schema for creating a payment"""

class PaymentResponse(PaymentBase):
    """Schema for response of payment"""
    payment_id : int

    class Config:
        """ ORM mode to convert SQLAlchemy models to Pydantic models """
        from_attributes = True
