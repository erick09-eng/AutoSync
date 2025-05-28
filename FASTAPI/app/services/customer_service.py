"""
customer_service.py
Service for managing customers.
This module contains the functions to interact with the customers table in the database.
It includes functions to create, read, update, and delete customers.
"""
from repositories import customers_repository as CustomersRepository
from schemas.customer_schema import CustomerCreate as CustomersCreate
from sqlalchemy.orm import Session


def create_customer(db: Session, customer: CustomersCreate):
    """Create a new customer in the database."""
    return CustomersRepository.create_customer(db, customer)


def get_customer(db: Session, customer_id: int):
    """Get a customer by its ID."""
    return CustomersRepository.get_customer(db, customer_id)


def get_all_customers(db: Session):
    """Get all customers."""
    return CustomersRepository.get_all_customers(db)


def update_customer(db: Session, customer_id: int, customer: CustomersCreate):
    """Update a customer by its ID."""
    return CustomersRepository.update_customer(db, customer_id, customer)


def delete_customer(db: Session, customer_id: int):
    """Delete a customer by its ID."""
    return CustomersRepository.delete_customer(db, customer_id)
