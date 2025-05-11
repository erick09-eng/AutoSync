from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SaleBase(BaseModel):
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
    pass

class SaleUpdate(SaleBase):
    pass

class SaleResponse(SaleBase):
    sale_id: int

    class Config:
        from_attributes = True
