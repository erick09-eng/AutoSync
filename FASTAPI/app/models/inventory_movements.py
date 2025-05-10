# models/inventory_movements.py
"""
This module defines the InventoryMovements model, which represents the
inventory movements in the system. It includes attributes such as movement ID,
product ID, user ID, movement type, quantity, reference ID, notes, and creation
timestamp.
"""

from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base

# pylint: disable=too-few-public-methods
class InventoryMovements(Base):
    """
    Represents an inventory movement in the database.
    Attributes:
        movement_id (int): The unique identifier for the inventory movement.
        product_id (int): The ID of the product associated with the movement.
        user_id (int): The ID of the user who performed the movement.
        movement_type (str): The type of movement (e.g., purchase, sale).
        quantity (int): The quantity of the product moved.
        reference_id (int): A reference ID for the movement.
        notes (str): Additional notes about the movement.
        created_at (datetime): The timestamp when the movement was created.
    """
    __tablename__ = "inventory_movements"

    movement_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)  # Foreign key to products table
    user_id = Column(Integer, index=True)  # Foreign key to users table
    movement_type = Column(String, index=True)  # purchase, sale, adjustment
    quantity = Column(Integer)
    reference_id = Column(Integer, index=True)
    notes = Column(String)  # Additional notes about the movement
    created_at = Column(DateTime)  # Timestamp of when the movement was created
