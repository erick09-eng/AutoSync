from sqlalchemy.orm import Session

from schemas.SaleSchema import SaleCreate as SalesCreate, SaleUpdate
from repositories import sales_repository

def create_sale(db: Session, sale: SalesCreate):
    return sales_repository.create_sale(db, sale)


def get_sale(db: Session, sale_id: int):
    return sales_repository.get_sale(db, sale_id=sale_id)

def get_sale(db: Session, sale_id: int):
    return sales_repository.get_sale(db, sale_id=sale_id)

def update_sale(db: Session, sale_id: int, sale: SaleUpdate):
    return sales_repository.update_sale(db, sale_id=sale_id, sale=sale)

def delete_sale(db: Session, sale_id: int):
    return sales_repository.delete_sale(db, sale_id=sale_id)