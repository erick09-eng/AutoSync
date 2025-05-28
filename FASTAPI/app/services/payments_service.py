# app/services/payments_service.py
"""
This module contains the business logic for handling payment-related operations.
It interacts with the database through the repository layer and handles
exceptions that may occur during these operations.
It provides functions to create, retrieve, update, and delete payment records.
"""
from models.payments import Payments
from repositories.payments_repository import (
    create_payment,
    get_payment,
    get_all_payments,
    update_payment,
    delete_payment,
)
from schemas.payments import PaymentCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_new_payment(db: Session, payment: PaymentCreate) -> Payments:
    """
    Create a new payment record in the database.
    """
    try:
        new_payment = create_payment(db, payment)
        return new_payment
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating payment: {str(e)}") from e

def get_payment_by_id(db: Session, payment_id: int) -> Payments:
    """
    Retrieve a payment record by its ID.
    """
    try:
        payment = get_payment(db, payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return payment
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving payment: {str(e)}") from e

def get_all_payments_list(db: Session) -> list[Payments]:
    """
    Retrieve all payment records.
    """
    try:
        payments = get_all_payments(db)
        return payments
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving payments: {str(e)}") from e

def update_existing_payment(db: Session, payment_id: int, payment: PaymentCreate) -> Payments:
    """
    Update an existing payment record.
    """
    try:
        updated_payment = update_payment(db, payment_id, payment)
        if not updated_payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return updated_payment
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating payment: {str(e)}") from e

