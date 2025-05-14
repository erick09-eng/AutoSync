#schemas/payment_methods.py
""" Schemas for payment methods """
from pydantic import BaseModel

class PaymentMethodBase(BaseModel):
    """ Base schema for payment methods """
    payment_method_name : str
    description : str
    requires_authorization : bool
    
class PaymentMethodCreate(PaymentMethodBase):
    """ Schema for creating a payment method """

class PaymentMethodResponse(PaymentMethodBase):
    """ Schema for response of payment method """
    payment_method_id : int
    
    class Config:
        """ ORM mode to convert SQLAlchemy models to Pydantic models """
        from_attributes = True
