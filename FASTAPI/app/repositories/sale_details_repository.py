
# repositories/sale_details_repository.py
from sqlalchemy.orm import Session
from models.sale_details import Sale_details
from schemas.sale_details import SaleDetailCreate


def create_sale_detail(db: Session, item: SaleDetailCreate):
    db_sale_detail = Sale_details(**Sale_details.dict())
    db.add(db_sale_detail)
    db.commit()
    db.refresh(db_sale_detail)
    return db_sale_detail


def get_sale_detail(db: Session, sale_detail_id: int):
    return db.query(Sale_details).filter(Sale_details.sale_detail_id == sale_detail_id).first()

def get_all_sale_details(db: Session):
    return db.query(Sale_details).all()








