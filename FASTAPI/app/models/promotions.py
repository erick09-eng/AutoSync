# models/promotions.py
"""
This module defines the Promotions model, which represents the promotions 
available in the system.

The Promotions table includes:
- `promotion_id`: The primary key for the promotion.
- `name`: The name of the promotion.
- `description`: A brief description of the promotion.
- `discount_type`: The type of discount (e.g., percentage).
- `discount_value`: The value of the discount.
- `start_date`: The start date of the promotion.
- `end_date`: The end date of the promotion.
- `is_active`: A boolean indicating whether the promotion is active.
- `created_at`: The timestamp when the promotion was created.
"""

from sqlalchemy import Column, Integer, String, Double, Boolean, DateTime
from db.database import Base

# pylint: disable=too-few-public-methods
class Promotions(Base):
    """
    Represents a promotion in the database.
    Attributes:
        promotion_id (int): The unique identifier for the promotion.
        name (str): The name of the promotion.
        description (str): A description of the promotion.
        discount_type (str): The type of discount (e.g., percentage).
        discount_value (float): The value of the discount.
        start_date (datetime): The start date of the promotion.
        end_date (datetime): The end date of the promotion.
        is_active (bool): Indicates if the promotion is active.
        created_at (datetime): The timestamp when the promotion was created.
    """
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
