# api/v1/sale_details_routes.py
"""FastAPI router for sale details endpoints."""
from schemas.sale_details import SaleDetailCreate, SaleDetailResponse
from services.sale_details_service import(
    create_sale_detail_service,
    get_sale_detail_service,
)
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=SaleDetailResponse)
def create_sale_detail(sale_detail: SaleDetailCreate,
                       db: Session = Depends(get_db)):
    """
    Create a new sale detail.
    """
    return create_sale_detail_service(db, sale_detail)

@router.get("/{sale_detail_id}", response_model=SaleDetailResponse)
def read_sale_detail(sale_detail_id: int,
                     db: Session = Depends(get_db)):
    """
    Get a sale detail by ID.
    """
    db_sale_detail = get_sale_detail_service(db, sale_detail_id)
    if db_sale_detail is None:
        raise HTTPException(status_code=404, detail="Sale detail not found")
    return db_sale_detail
