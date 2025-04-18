# models/item.py
from sqlalchemy import Column, Integer, String, Timestamp
from db.database import Base


class Item(Base):
    __tablename__ = "inventory_movements"

    movement_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)  # Foreign key to products table
    user_id = Column(Integer, index=True)  # Foreign key to users table
    movement_type = Column(String, index=True)  # purchase, sale, adjustment
    quantity = Column(Integer)
    reference_id = Column(Integer, index=True)
    notes = Column(String)  # Additional notes about the movement
    created_at = Column(Timestamp)  # Timestamp of when the movement was created

