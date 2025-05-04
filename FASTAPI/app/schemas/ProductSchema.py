from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    sku: Optional[str] = None
    name: str
    description: Optional[str]
    category_id: int
    unit_price: float
    cost_price: Optional[float]
    current_stock: int
    min_stock: int
    on_offer: Optional[bool] = False
    offer_price: Optional[float] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    product_id: int

    class Config:
        from_attributes = True
