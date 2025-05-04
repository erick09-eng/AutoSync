#schemas/promotions.py
from pydantic import BaseModel
from datetime import datetime

class PromotionsBase(BaseModel):
    name : str
    description : str
    discount_type : str
    discount_value : float
    start_date : datetime
    end_date : datetime
    is_active : bool
    created_at : datetime
    # created_at : datetime = datetime.now()  # Default to current time

class PromotionsCreate(PromotionsBase):
    pass

class PromotionsResponse(PromotionsBase):
    promotion_id : int

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models