# app/models/sale_details.py
"""Sale_details model module.

This module contains the SQLAlchemy ORM model for sale details.

Classes:
    Sale_details: Represents a sale detail record.

"""

from sqlalchemy import Column, Integer, Double, ForeignKey
from db.database import Base

class SaleDetails(Base):
    """Represents a sale detail.

    Attributes:
        sale_detail_id (int): Primary key for the sale detail.
        sale_id (int): Foreign key to the sales table.
        product_id (int): Foreign key to the products table.
        quantity (int): Quantity sold.
        unit_price (float): Unit price of the product.
        discount_percentage (float): Discount percentage applied.
        subtotal (float): Subtotal amount.
    """

    __tablename__ = "sale_details"

    sale_detail_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), index=True) # Foreign key to sales table
    product_id = Column(Integer,ForeignKey("products.product_id"), index=True) # Foreign key to products table
    quantity = Column(Integer, index=True)
    unit_price = Column(Double, index=True)
    discount_percentage = Column(Double, index=True)
    subtotal = Column(Double)
