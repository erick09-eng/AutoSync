#app/api/v1/sales_router.py
"""FastAPI router for sales endpoints."""
from services.sales_service import (
    create_sale,
    get_sale,
    update_sale,
    get_all_sales
)
from schemas.sale_schema import SaleCreate, SaleUpdate, SaleResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=SaleResponse)
def create(sale: SaleCreate, db: Session = Depends(get_db)):
    """Create a new sale.
    """
    return create_sale(db, sale)

@router.get("/{sale_id}", response_model=SaleResponse)
def read(sale_id: int, db: Session = Depends(get_db)):
    """Get a sale by ID.
    """
    db_sale = get_sale(db, sale_id)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.put("/{sale_id}", response_model=SaleResponse)
def update(sale_id: int, sale: SaleUpdate,
           db: Session = Depends(get_db)):
    """Update a sale by ID.
    """
    return update_sale(db, sale_id, sale)

@router.get("/", response_model=list[SaleResponse])
def read_all(db: Session = Depends(get_db)):
    """Get all sales.
    """
    return get_all_sales(db)
