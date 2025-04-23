# api/v1/payment_methods_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List

from schemas.payment_methods import PaymentMethodCreate, PaymentMethodResponse
from services.payment_methods_service import create_payment_method_service, get_payment_method_service, get_all_payment_methods_service
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=PaymentMethodResponse)
def create_payment_method(payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    return create_payment_method_service(db, payment_method)

@router.get("/{payment_method_id}", response_model=List[PaymentMethodResponse])
def read_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    db_payment_method = get_payment_method_service(db, payment_method_id)
    if db_payment_method is None:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return db_payment_method

@router.get("/", response_model=list[PaymentMethodResponse])
def read_payment_methods(db: Session = Depends(get_db)):
    return get_all_payment_methods_service(db)


