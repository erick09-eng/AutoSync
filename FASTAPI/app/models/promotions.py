# app/models/promotions.py
"""Promotions model module.

This module contains the SQLAlchemy ORM model for promotions.

Classes:
    Promotions: Represents a promotion.

"""

from sqlalchemy import Column, Integer, String, Double, Boolean, DateTime
from db.database import Base

# pylint: disable=too-few-public-methods
class Promotions(Base):
    """Represents a promotion.

    Attributes:
        promotion_id (int): Primary key for the promotion.
        name (str): Name of the promotion.
        description (str): Description of the promotion.
        discount_type (str): Type of discount (e.g., percentage).
        discount_value (float): Value of the discount.
        start_date (datetime): Start date of the promotion (YYYY-MM-DD).
        end_date (datetime): End date of the promotion (YYYY-MM-DD).
        is_active (bool): Indicates if the promotion is active.
        created_at (datetime): Timestamp when the promotion was created.
    """

    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    discount_type = Column(String(255))  # percentage
    discount_value = Column(Double)
    start_date = Column(DateTime)  # YYYY-MM-DD
    end_date = Column(DateTime)  # YYYY-MM-DD
    is_active = Column(Boolean)  # 1 for active, 0 for inactive
    created_at = Column(DateTime)  # YYYY-MM-DD
