from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from db.database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, nullable=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    unit_price = Column(Float, nullable=False)
    cost_price = Column(Float, nullable=True)
    current_stock = Column(Integer)
    min_stock = Column(Integer)
    on_offer = Column(Boolean, default=False)
    offer_price = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
