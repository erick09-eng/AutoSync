#repositories/inventory_movements_repository.py
from sqlalchemy.orm import Session
from models import inventory_movements as Inventory_movements
from schemas.inventory_movements import InventoryMovementCreate, InventoryMovementResponse

def create_movement(db: Session, movement: InventoryMovementCreate):
    db_movement = Inventory_movements(**movement.dict())
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement

def get_movement(db: Session, movement_id: int):
    return db.query(Inventory_movements).filter(Inventory_movements.movement_id == movement_id).first()

def get_all_movements(db: Session):
    return db.query(Inventory_movements).all()
