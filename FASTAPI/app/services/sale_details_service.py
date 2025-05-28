# app/services/sale_details_service.py
""""
This module defines the service layer for handling sale details in the system.
It includes functions for creating and retrieving sale details.
"""
from sqlalchemy.orm import Session
from repositories.sale_details_repository import (
    create_sale_detail,
    get_sale_detail)
from schemas.sale_details import SaleDetailCreate

def create_sale_detail_service(db: Session, sale_detail: SaleDetailCreate):
    """Create a new sale detail in the database.
    Args:
        db (Session): The database session.
        sale_detail (SaleDetailCreate): The sale detail to create.
    Returns:
        SaleDetails: The created sale detail.
    """
    # Aquí se calcularia el subtotal
    return create_sale_detail(db, sale_detail)

def get_sale_detail_service(db: Session, sale_detail_id: int):
    """Get a sale detail by its ID.
    Args:
        db (Session): The database session.
        sale_detail_id (int): The ID of the sale detail to retrieve.
    Returns:
        SaleDetails: The sale detail with the specified ID.
    """
    return get_sale_detail(db, sale_detail_id)
