#app/services/inventory_movements_service.py
"""
This module defines the service layer for handling inventory movements in the system.
It includes functions for creating and retrieving inventory movements.
"""

from repositories.inventory_movements_repository import (
    create_movement,
    get_movement,
    get_all_movements,
    update_movement,
)
from schemas.inventory_movements import InventoryMovementCreate
from sqlalchemy.orm import Session

def create_movement_service(db: Session, movement: InventoryMovementCreate):
    """Create a new inventory movement in the database.
    Args:
        db (Session): The database session.
        movement (InventoryMovementCreate): The inventory movement to create.
    Returns:
        InventoryMovements: The created inventory movement.
    """
    return create_movement(db, movement)

def get_movement_service(db: Session, movement_id: int):
    """Get an inventory movement by its ID.
    Args:
        db (Session): The database session.
        movement_id (int): The ID of the inventory movement to retrieve.
    Returns:
        InventoryMovements: The inventory movement with the specified ID.
    """
    return get_movement(db, movement_id)

def get_all_movements_service(db: Session):
    """Get all inventory movements.
    Args:
        db (Session): The database session.
    Returns:
        List[InventoryMovements]: A list of all inventory movements.
    """
    return get_all_movements(db)

def update_movement_service(db: Session, movement_id: int,
                            movement: InventoryMovementCreate):
    """Update an existing inventory movement.
    Args:
        db (Session): The database session.
        movement_id (int): The ID of the inventory movement to update.
        movement (InventoryMovementCreate): The updated inventory movement data.
    Returns:
        InventoryMovements: The updated inventory movement.
    """
    return update_movement(db, movement_id, movement)
