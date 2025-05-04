#schemas/inventory_movements.py
from pydantic import BaseModel
from datetime import datetime

class InventoryMovementBase(BaseModel):
    
    product_id : int
    user_id : int
    movement_type : str
    quantity : int
    reference_id : int
    notes : str
    created_at : datetime
    

class InventoryMovementCreate(InventoryMovementBase):
    pass

class InventoryMovementResponse(InventoryMovementBase):
    movement_id: int

    class Config:
        from_attributes: True
