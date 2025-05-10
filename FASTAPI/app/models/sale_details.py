# models/sale_details.py
""""
This module defines the SaleDetails model, which represents the details of a sale
in the system. It includes attributes such as sale detail ID, sale ID, product ID,
quantity, unit price, discount percentage, and subtotal.
"""
from sqlalchemy import Column, Integer, Double, ForeignKey
from db.database import Base

# pylint: disable=too-few-public-methods
class SaleDetails(Base):
    """
    Represents the details of a sale in the database.
    Attributes:
        sale_detail_id (int): The unique identifier for the sale detail.
        sale_id (int): The ID of the sale associated with this detail.
        product_id (int): The ID of the product associated with this detail.
        quantity (int): The quantity of the product sold.
        unit_price (float): The unit price of the product.
        discount_percentage (float): The discount percentage applied to the product.
        subtotal (float): The subtotal amount for this sale detail.
    """
    __tablename__ = "sale_details"

    sale_detail_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), index=True) # Foreign key to sales table
    product_id = Column(Integer, index=True) # Foreign key to products table
    quantity = Column(Integer, index=True)
    unit_price = Column(Double, index=True)
    discount_percentage = Column(Double, index=True)
    subtotal = Column(Double)
