#schemas/payment_methods.py
from pydantic import BaseModel

class PaymentMethodBase(BaseModel):
  
    name : str
    description : str
    requieres_authorization : bool
    
class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodResponse(PaymentMethodBase):
    payment_method_id : int
    
    class Config:
        orm_mode = True
            
    
 