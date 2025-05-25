#app/api/v1/inventory_movements_router.py
"""
Inventory Movements Router
This module defines the API endpoints for managing inventory movements.
It includes endpoints for creating, retrieving, and listing inventory movements.
"""
from typing import List
from services.inventory_movements_service import (
    create_movement_service,
    get_movement_service,
    get_all_movements_service,
    update_movement_service,
    )
from schemas.inventory_movements import(InventoryMovementCreate, 
                                        InventoryMovementResponse
    ) 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=InventoryMovementResponse)
def create_movement(movement: InventoryMovementCreate,
                    db: Session = Depends(get_db)):
    """
    Create a new inventory movement.
    """
    return create_movement_service(db, movement)

@router.get("/{movement_id}", response_model=InventoryMovementResponse)
def read_movement(movement_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific inventory movement by its ID."""
    db_movement = get_movement_service(db, movement_id)
    if db_movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return db_movement

@router.get("/", response_model=List[InventoryMovementResponse])
def list_movements(db: Session = Depends(get_db)):
    """Retrieve a list of all inventory movements."""
    return get_all_movements_service(db)

@router.put("/{movement_id}", response_model=InventoryMovementResponse)
def update_movement(movement_id: int,
                    movement: InventoryMovementCreate,
                    db: Session = Depends(get_db)):
    """Update an existing inventory movement."""
    db_movement = update_movement_service(db, movement_id, movement)
    if db_movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return db_movement
