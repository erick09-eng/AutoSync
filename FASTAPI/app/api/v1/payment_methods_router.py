# api/v1/payment_methods_router.py
"""FastAPI router for payment methods."""
from schemas.payment_methods import PaymentMethodCreate, PaymentMethodResponse
from services.payment_methods_service import(
    create_payment_method_service,
    get_payment_method_service,
    get_all_payment_methods_service,
    update_payment_method_service,
    delete_payment_method_service
)
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=PaymentMethodResponse)
def create_payment_method(payment_method: PaymentMethodCreate,
                          db: Session = Depends(get_db)):
    """Create a new payment method."""
    return create_payment_method_service(db, payment_method)

@router.get("/{payment_method_id}", response_model=PaymentMethodResponse)
def read_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    """Get a payment method by ID."""
    db_payment_method = get_payment_method_service(db, payment_method_id)
    if db_payment_method is None:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return db_payment_method

@router.get("/", response_model=list[PaymentMethodResponse])
def read_payment_methods(db: Session = Depends(get_db)):
    """Get all payment methods."""
    return get_all_payment_methods_service(db)

@router.put("/{payment_method_id}", response_model=PaymentMethodResponse)
def update_payment_method(
    payment_method_id: int,
    payment_method: PaymentMethodCreate,
    db: Session = Depends(get_db)
):
    """Update a payment method."""
    db_payment_method = update_payment_method_service(db, payment_method_id, payment_method)
    if not db_payment_method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return db_payment_method

@router.delete("/{payment_method_id}", response_model=PaymentMethodResponse)
def delete_payment_method(payment_method_id: int,
                          db: Session = Depends(get_db)):
    """Delete a payment method."""
    db_payment_method = delete_payment_method_service(db, payment_method_id)
    if not db_payment_method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return db_payment_method
