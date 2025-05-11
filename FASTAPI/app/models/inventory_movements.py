"""Inventory_movements model module.

This module contains the SQLAlchemy ORM model for tracking inventory movements.

Classes:
    Inventory_movements: Represents an inventory movement record.

"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.database import Base


class Inventory_movements(Base):
    """Represents an inventory movement.

    Attributes:
        movement_id (int): Primary key for the inventory movement.
        product_id (int): Foreign key to the products table.
        user_id (int): Foreign key to the users table.
        movement_type (str): Type of movement (purchase, sale, adjustment).
        quantity (int): Quantity moved.
        reference_id (int): Reference ID related to the movement.
        notes (str): Additional notes about the movement.
        created_at (datetime): Timestamp when the movement was created.
    """

    __tablename__ = "inventory_movements"

    movement_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer,ForeignKey("products.product_id"), index=True)  # Foreign key to products table
    user_id = Column(Integer, ForeignKey("users.user_id"),index=True)  # Foreign key to users table
    movement_type = Column(String(255), index=True)  # purchase, sale, adjustment
    quantity = Column(Integer)
    reference_id = Column(Integer, index=True)
    notes = Column(String(255))  # Additional notes about the movement
    created_at = Column(DateTime)  # Timestamp of when the movement was created
