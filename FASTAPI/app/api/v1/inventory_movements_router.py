from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.inventory_movements_service import (
    create_movement_service,
    get_movement_service,
    get_all_movements_service
)
from schemas.inventory_movements import InventoryMovementCreate, InventoryMovementResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=InventoryMovementResponse)
def create_movement(movement: InventoryMovementCreate, db: Session = Depends(get_db)):
    return create_movement_service(db, movement)

@router.get("/{movement_id}", response_model=InventoryMovementResponse)
def read_movement(movement_id: int, db: Session = Depends(get_db)):
    db_movement = get_movement_service(db, movement_id)
    if db_movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return db_movement

@router.get("/", response_model=List[InventoryMovementResponse])
def list_movements(db: Session = Depends(get_db)):
    return get_all_movements_service(db)
