#app/schemas/inventory_movements.py
"""
Inventory Movements Schema
This module contains the Pydantic schemas for the inventory movements.
It includes schemas for creating, updating, and responding with inventory movements.
"""
# pylint: disable=too-few-public-methods
from datetime import datetime
from pydantic import BaseModel

class InventoryMovementBase(BaseModel):
    """Base Inventory Movement Schema"""
    product_id : int
    user_id : int
    movement_type : str
    quantity : int
    reference_id : int
    notes : str
    created_at : datetime

class InventoryMovementCreate(InventoryMovementBase):
    """Create Inventory Movement Schema"""

class InventoryMovementResponse(InventoryMovementBase):
    """Response Inventory Movement Schema"""
    movement_id: int

    class Config:
        """ Pydantic Config"""
        from_attributes: True
