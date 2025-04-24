#schemas/payments.py
from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    sale_id : int
    payment_method_id : int
    amount : float
    transaction_code : str
    payment_date = datetime
    status : str 
    
class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id : int
    
    class Config:
        orm_mode = True

