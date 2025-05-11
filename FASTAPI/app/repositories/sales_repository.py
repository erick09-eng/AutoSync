from sqlalchemy.orm import Session

from models import sales as Sales
from schemas.SaleSchema import SaleCreate as SalesCreate, SaleResponse as SalesResponse
from datetime import datetime

def create_sale(db: Session, sale: SalesCreate):
    db_sale = Sales(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sale(db: Session, sale_id: int):
    return db.query(Sales).filter(Sales.id == sale_id).first()

def get_all_sales(db: Session):
    return db.query(Sales).all()

def update_sale(db: Session, sale_id: int, sale: SalesCreate):
    db_sale = get_sale(db, sale_id)
    if db_sale:
        for key, value in sale.dict().items():
            setattr(db_sale, key, value)
        db.commit()
        
def delete_sale(db: Session, sale_id: int):
    db_sale = get_sale(db, sale_id)
    if db_sale:
        db.delete(db_sale)
        db.commit()
        return True
    return False