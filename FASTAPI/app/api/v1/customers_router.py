#app/api/v1/customers_router.py
"""Customer API router module.
This module contains the FastAPI router for customer-related operations.
It provides endpoints for creating, reading, updating, and deleting customers.
"""
from services.customer_service import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)
from schemas.customer_schema import CustomerCreate, CustomerResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
def create(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a new customer."""
    return create_customer(db, customer)

@router.get("/{customer_id}", response_model=CustomerResponse)
def read(customer_id: int, db: Session = Depends(get_db)):
    """Get a customer by its ID."""
    db_customer = get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=list[CustomerResponse])
def list_all(db: Session = Depends(get_db)):
    """Get all customers."""
    return get_all_customers(db)

@router.put("/{customer_id}", response_model=CustomerResponse)
def update(customer_id: int, customer: CustomerCreate,
           db: Session = Depends(get_db)):
    """Update an existing customer."""
    return update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    """Delete a customer."""
    return delete_customer(db, customer_id)
