# models/Sale_details.py
from sqlalchemy import Column, Integer, Double, ForeignKey
from db.database import Base


class Sale_details(Base):
    __tablename__ = "sale_details"

    sale_detail_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), index=True) # Foreign key to sales table
    product_id = Column(Integer, index=True) # Foreign key to products table
    quantity = Column(Integer, index=True)
    unit_price = Column(Double, index=True)
    discount_percentage = Column(Double, index=True)
    subtotal = Column(Double)
    
    

