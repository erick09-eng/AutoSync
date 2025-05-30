#app/services/payment_methods_service.py
"""
This module contains services related to payment methods.
It provides functions to create, retrieve, and fetch all payment methods from the database.

Functions:
    create_payment_method_service(db: Session, payment_method: PaymentMethodCreate):
        Creates a new payment method in the database.
    get_payment_method_service(db: Session, payment_method_id: int):
        Retrieves a payment method by its ID.
    get_all_payment_methods_service(db: Session):
        Retrieves all registered payment methods.
"""
from repositories.payment_methods_repository import (
    create_payment_method,
    get_payment_method,
    get_all_payment_methods,
    update_payment_method,
    delete_payment_method,
)
from schemas.payment_methods import PaymentMethodCreate
from sqlalchemy.orm import Session

def create_payment_method_service(db: Session, payment_method: PaymentMethodCreate):
    """
    Create a new payment method in the database.
    Args:
        db (Session): The database session.
        payment_method (PaymentMethodCreate): The payment method to create.
    Returns:
        The created payment method.
    """
    return create_payment_method(db, payment_method)

def get_payment_method_service(db: Session, payment_method_id: int):
    """
    Get a payment method by its ID.
    Args:
        db (Session): The database session.
        payment_method_id (int): The ID of the payment method to retrieve.
    Returns:
        The payment method with the specified ID.
    """
    return get_payment_method(db, payment_method_id)

def get_all_payment_methods_service(db: Session):
    """
    Get all payment methods.
    Args:
        db (Session): The database session.
    Returns:
        A list of all payment methods.
    """
    return get_all_payment_methods(db)

def update_payment_method_service(db: Session, payment_method_id: int,
                                  payment_method: PaymentMethodCreate):
    """
    Update a payment method by its ID.
    Args:
        db (Session): The database session.
        payment_method_id (int): The ID of the payment method to update.
        payment_method (PaymentMethodCreate): The updated payment method data.
    Returns:
        The updated payment method.
    """
    return update_payment_method(db, payment_method_id, payment_method)

def delete_payment_method_service(db: Session, payment_method_id: int):
    """
    Delete a payment method by its ID.
    Args:
        db (Session): The database session.
        payment_method_id (int): The ID of the payment method to delete.
    Returns:
        The deleted payment method.
    """
    return delete_payment_method(db, payment_method_id)
