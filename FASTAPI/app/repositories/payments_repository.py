#app/repositories/payments_repository.py
"""
Payments Repository
This module contains functions to interact with the Payments table in the database.
It includes functions to create, read, update, and delete payment records.
"""
from models.payments import Payments
from schemas.payments import PaymentCreate
from sqlalchemy.orm import Session

def create_payment(db: Session, payment: PaymentCreate):
    """Create a new payment record in the database."""
    try:
        # Convert the PaymentCreate schema to a Payments model instance
        db_payment = Payments(
            **payment.dict())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except Exception as e:
        db.rollback()
        raise e from e

def get_payment(db: Session, payment_id: int):
    """Get a payment record by its ID."""
    return db.query(Payments).filter(
        Payments.payment_id == payment_id).first()

def get_all_payments(db: Session):
    """Get all payment records."""
    return db.query(Payments).all()

def update_payment(
    db: Session,
    payment_id: int,
    payment: PaymentCreate):
    """Update an existing payment record."""
    db_payment = db.query(Payments).filter(
        Payments.payment_id == payment_id).first()
    if db_payment:
        for key, value in payment.dict().items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment

