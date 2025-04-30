from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.sales_service import (
    create_sale,
    get_sale,
    update_sale,
    delete_sale,
)
from schemas.sales_schema import SaleCreate, SaleUpdate, SaleResponse

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

@router.post("/", response_model=SaleResponse)
def create(sale: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db, sale)

@router.get("/{sale_id}", response_model=SaleResponse)
def read(sale_id: int, db: Session = Depends(get_db)):
    db_sale = get_sale(db, sale_id)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.put("/{sale_id}", response_model=SaleResponse)
def update(sale_id: int, sale: SaleUpdate, db: Session = Depends(get_db)):
    return update_sale(db, sale_id, sale)

@router.delete("/{sale_id}")
def delete(sale_id: int, db: Session = Depends(get_db)):
    return delete_sale(db, sale_id)
