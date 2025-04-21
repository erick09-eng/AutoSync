#schemas/product_promotions.py
from pydantic import BaseModel
from datetime import datetime

class ProductPromotionsBase(BaseModel):
    product_id = int
    promotion_id = int
    
class ProductPromotionsCreate(ProductPromotionsBase):
    pass

## TODO review this
class ProductPromotionsResponse(ProductPromotionsBase):
    product_promotion_id: int
    created_at: datetime

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models