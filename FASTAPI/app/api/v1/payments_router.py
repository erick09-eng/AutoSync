#api/v1/payments_router.py
"""FastAPI router for payments."""
from typing import List
from services.payments_service import (
    create_new_payment,
    get_payment_by_id,
    get_all_payments_list,
    update_existing_payment,
)
from schemas.payments import PaymentCreate, PaymentResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()
@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    """
    Create a new payment record.
    """
    return create_new_payment(db, payment)

@router.get("/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a payment record by its ID.
    """
    db_payment = get_payment_by_id(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.get("/", response_model=List[PaymentResponse])
def list_payments(db: Session = Depends(get_db)):
    """
    Retrieve all payment records.
    """
    return get_all_payments_list(db)

@router.put("/{payment_id}", response_model=PaymentResponse)
def update_payment(payment_id: int, payment: PaymentCreate, db: Session = Depends(get_db)):
    """
    Update an existing payment record.
    """
    db_payment = update_existing_payment(db, payment_id, payment)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
