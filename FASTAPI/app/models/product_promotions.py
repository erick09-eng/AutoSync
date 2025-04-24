# models/product_promotions.py
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey
from db.database import Base


class Product_Promotions(Base):
    __tablename__ = "product_promotions"

    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.promotion_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', 'promotion_id'),
    )
