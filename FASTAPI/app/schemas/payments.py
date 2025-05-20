#app/schemas/payments.py
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

