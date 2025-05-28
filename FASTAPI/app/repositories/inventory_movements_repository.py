#app/repositories/inventory_movements_repository.py
"""
Inventory Movements Repository
This module contains the functions to interact with the inventory movements table in the database.
It includes functions to create, read, update, and delete inventory movements.
"""
from models.inventory_movements import InventoryMovements
from schemas.inventory_movements import InventoryMovementCreate
from sqlalchemy.orm import Session

def create_movement(db: Session, movement: InventoryMovementCreate):
    """Create a new inventory movement in the database.
    Args:
        db (Session): The database session.
        movement (InventoryMovementCreate): The inventory movement to create.
    Returns:
        Inventory_movements: The created inventory movement.
    """
    db_movement = InventoryMovements(**movement.dict())
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement

def get_movement(db: Session, movement_id: int):
    """Get an inventory movement by its ID.
    Args:
        db (Session): The database session.
        movement_id (int): The ID of the inventory movement to retrieve.
    Returns:
        Inventory_movements: The inventory movement with the specified ID.
    """
    return db.query(InventoryMovements).filter(
        InventoryMovements.movement_id == movement_id).first()

def get_all_movements(db: Session):
    """Get all inventory movements.
    Args:
        db (Session): The database session.
    Returns:
        List[Inventory_movements]: A list of all inventory movements.
    """
    return db.query(InventoryMovements).all()

def update_movement(db: Session, movement_id: int, movement: InventoryMovementCreate):
    """Update an inventory movement by its ID.
    Args:
        db (Session): The database session.
        movement_id (int): The ID of the inventory movement to update.
        movement (InventoryMovementCreate): The updated inventory movement data.
    Returns:
        Inventory_movements: The updated inventory movement.
    """
    db_movement = get_movement(db, movement_id)
    if db_movement:
        for key, value in movement.dict().items():
            setattr(db_movement, key, value)
        db.commit()
        db.refresh(db_movement)
    return db_movement
