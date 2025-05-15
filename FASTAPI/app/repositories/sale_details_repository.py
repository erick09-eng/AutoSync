#app/repositories/sale_details_repository.py
"""
This module contains the repository layer for handling sale detail-related operations.
It interacts with the database and provides functions to create, retrieve,
and list sale detail records.
It abstracts the database operations and provides a clean interface for the service layer.
It provides functions to create, retrieve, and list sale detail records.
"""
from typing import Optional, List
from models.sale_details import SaleDetails
from schemas.sale_details import SaleDetailCreate
from sqlalchemy.orm import Session

def create_sale_detail(
    db: Session,
    sale_detail:
    SaleDetailCreate) -> SaleDetails:
    """
    Create a new sale detail record in the database.
    """
    db_sale_detail = SaleDetails(**sale_detail.dict())
    db.add(db_sale_detail)
    db.commit()
    db.refresh(db_sale_detail)
    return db_sale_detail

def get_sale_detail(db: Session, sale_detail_id: int) -> Optional[SaleDetails]:
    """
    Retrieve a sale detail record by its ID.
    """
    return db.query(SaleDetails).filter(SaleDetails.sale_detail_id == sale_detail_id).first()

def get_all_sale_details(db: Session) -> List[SaleDetails]:
    """
    Retrieve all sale detail records.
    """
    return db.query(SaleDetails).all()
