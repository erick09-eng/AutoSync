#app/repositories/payment_methods_repository.py
"""
This file contains the repository functions for payment methods.
It includes functions to create, read, update, and delete payment methods.
"""
from models.payment_methods import PaymentMethod
from schemas.payment_methods import PaymentMethodCreate
from sqlalchemy.orm import Session

def create_payment_method(db: Session, payment_method: PaymentMethodCreate):
    """Create a new payment method in the database."""
    # Check if the payment method already exists
    existing_payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_name == payment_method.payment_method_name
    ).first()
    if existing_payment_method:
        return None
    # Create a new payment method
    db_payment_method = PaymentMethod(**payment_method.dict())
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method

def get_payment_method(db: Session, payment_method_id: int):
    """Get a payment method by its ID."""
    # Check if the payment method exists
    if not db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first():
        return None
    # Return the payment method
    return db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first()

def get_all_payment_methods(db: Session):
    """Get all payment methods."""
    # Return all payment methods
    return db.query(PaymentMethod).all()

def update_payment_method(
    db: Session,
    payment_method_id: int,
    payment_method: PaymentMethodCreate):
    """Update a payment method."""
    # Check if the payment method exists
    if not db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first():
        return None
    # Update the payment method
    # Check if the payment method already exists
    existing_payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_name == payment_method.payment_method_name
    ).first()
    if existing_payment_method and existing_payment_method.payment_method_id != payment_method_id:
        return None
    # Update the payment method
    db_payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first()
    if db_payment_method:
        for key, value in payment_method.dict().items():
            setattr(db_payment_method, key, value)
        db.commit()
        db.refresh(db_payment_method)
    return db_payment_method

def delete_payment_method(db: Session, payment_method_id: int):
    """Delete a payment method."""
    # Check if the payment method exists
    if not db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first():
        return None
    # Delete the payment method
    # Check if the payment method already exists
    existing_payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id
    ).first()
    if not existing_payment_method:
        return None
    # Delete the payment method
    db_payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.payment_method_id == payment_method_id).first()
    if db_payment_method:
        db.delete(db_payment_method)
        db.commit()
    return db_payment_method
