#services/inventory_movements_service.py
from sqlalchemy.orm import Session
from repositories.inventory_movements_repository import create_movement, get_movement, get_all_movements
from schemas.inventory_movements import InventoryMovementCreate

def create_movement_service(db: Session, movement: InventoryMovementCreate):
    # TO DO Aquí se prondría la lógica de negocio (por ejemplo validar tipo de movimiento)
    return create_movement(db, movement)

def get_movement_service(db: Session, movement_id: int):
    return get_movement(db, movement_id)

def get_all_movements_service(db: Session):
    return get_all_movements(db)


