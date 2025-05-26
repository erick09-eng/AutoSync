# app/models/product_promotions.py
"""Product_promotions model module.

This module contains the SQLAlchemy ORM model for product promotions.

Classes:
    Product_Promotions: Represents a product promotion association.

"""

# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey
from db.database import Base


class ProductPromotions(Base):
    """Represents a product promotion association.

    Attributes:
        product_id (int): Foreign key to the products table.
        promotion_id (int): Foreign key to the promotions table.
    """

    __tablename__ = "product_promotions"

    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.promotion_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', 'promotion_id'),
    )
