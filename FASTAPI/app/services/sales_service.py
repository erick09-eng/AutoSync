#app/services/sales_service.py
"""Sales Service Module
This module contains the business logic for managing sales.
It interacts with the sales repository to perform CRUD operations.
"""
from schemas.sale_schema import SaleCreate as SalesCreate, SaleUpdate
from repositories import sales_repository
from sqlalchemy.orm import Session

def create_sale(db: Session, sale: SalesCreate):
    """Create a new sale."""
    return sales_repository.create_sale(db, sale)

def get_sale(db: Session, sale_id: int):
    """Get a sale by its ID."""
    return sales_repository.get_sale(db, sale_id = sale_id)

def update_sale(db: Session, sale_id: int, sale: SaleUpdate):
    """Update an existing sale."""
    return sales_repository.update_sale(db, sale_id=sale_id, sale=sale)

def get_all_sales(db: Session):
    """Get all sales."""
    return sales_repository.get_all_sales(db)