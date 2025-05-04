# models/Promotions.py
from sqlalchemy import Column, Integer, String, Double, Boolean, DateTime
from db.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    discount_type = Column(String)  # percentage
    discount_value = Column(Double)
    start_date = Column(DateTime)  # YYYY-MM-DD
    end_date = Column(DateTime)  # YYYY-MM-DD
    is_active = Column(Boolean)  # 1 for active, 0 for inactive
    created_at = Column(DateTime)  # YYYY-MM-DD
    

