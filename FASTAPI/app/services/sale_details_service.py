# services/sale_details_service.py
from sqlalchemy.orm import Session
from FASTAPI.app.repositories.sale_details_repository import create_sale_detail, get_all_sale_details, get_sale_detail
from schemas.sale_details import SaleDetailCreate


def create_sale_detail_service(db: Session, sale_detail: SaleDetailCreate):
     # Aquí se calcularia el subtotal 
    return create_sale_detail(db, sale_detail)
    


def get_sale_detail_service(db: Session, sale_detail_id: int):
    return get_sale_detail(db, sale_detail_id)


