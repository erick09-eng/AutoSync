"""
This module defines the Product_Promotions model, which represents the 
many-to-many relationship between products and promotions in the database.

The Product_Promotions table includes:
- `product_id`: A foreign key referencing the `products` table.
- `promotion_id`: A foreign key referencing the `promotions` table.

The combination of `product_id` and `promotion_id` serves as the primary key.
"""
# models/product_promotions.py

from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey
from db.database import Base

# pylint: disable=too-few-public-methods
class ProductPromotions(Base):
    """
    Represents the many-to-many relationship between products and promotions in the database.
    Attributes:
        product_id (int): A foreign key referencing the `products` table.
        promotion_id (int): A foreign key referencing the `promotions` table.
    """
    __tablename__ = "product_promotions"

    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.promotion_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', 'promotion_id'),
    )
