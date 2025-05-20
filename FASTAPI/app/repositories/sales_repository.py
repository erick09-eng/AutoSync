#app/repositories/sales_repository.py
"""Sales Repository Module
This module contains functions to interact with the Sales table in the database.
It includes functions to create, read, update, and delete sales records.
"""
from models import sales as Sales
from schemas.sale_schema import SaleCreate as SalesCreate
from sqlalchemy.orm import Session


def create_sale(db: Session, sale: SalesCreate):
    """
        Create a new sale in the database.
    """
    db_sale = Sales(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


def get_sale(db: Session, sale_id: int):
    """
        Get a sale by ID.
    """
    return db.query(Sales).filter(Sales.id == sale_id).first()


def get_all_sales(db: Session):
    """
        Get all sales records.
    """
    return db.query(Sales).all()


def update_sale(db: Session, sale_id: int, sale: SalesCreate):
    """
        Update an existing sale.
    """
    db_sale = get_sale(db, sale_id)
    if db_sale:
        for key, value in sale.dict().items():
            setattr(db_sale, key, value)
        db.commit()


def delete_sale(db: Session, sale_id: int):
    """
        Delete a sale by ID.
    """
    db_sale = get_sale(db, sale_id)
    if db_sale:
        db.delete(db_sale)
        db.commit()
        return True
    return False
