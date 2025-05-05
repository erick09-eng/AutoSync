#schemas/product_promotions.py
from pydantic import BaseModel
from datetime import datetime

class ProductPromotionsBase(BaseModel):
    product_id : int
    promotion_id : int
    
class ProductPromotionsCreate(ProductPromotionsBase):
    pass

class ProductPromotionsResponse(ProductPromotionsBase):

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models

