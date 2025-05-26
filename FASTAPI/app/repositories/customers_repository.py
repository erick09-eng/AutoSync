#app/repositories/customers_repository.py
"""Repository for managing customers in the database."""
from datetime import datetime,timezone, timedelta
from models.customers import Customers
from schemas.customer_schema import CustomerCreate

from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_colombia_time():
    """Get current time in Colombia timezone (UTC-5)."""
    colombia_tz = timezone(timedelta(hours=-5))
    return datetime.now(colombia_tz)

def create_customer(db: Session, customer: CustomerCreate):
    """Create a new customer in the database."""
    customer_data = customer.dict()
    customer_data['created_at'] = get_colombia_time()
    customer_data['updated_at'] = get_colombia_time()

    db_customer = Customers(**customer_data)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    """Retrieve a customer by their ID."""
    customer = db.query(Customers).filter(Customers.customer_id == customer_id).first()

    if customer:
        if not customer.created_at:
            customer.created_at = get_colombia_time()
        if not customer.updated_at:
            customer.updated_at = get_colombia_time()

    return customer


def get_all_customers(db: Session):
    """Retrieve all customers."""
    customers = db.query(Customers).all()

    for customer in customers:
        if not customer.created_at:
            customer.created_at = get_colombia_time()
        if not customer.updated_at:
            customer.updated_at = get_colombia_time()

    return customers

def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
    """Update an existing customer in the database."""
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail=f"Customer with id {customer_id} not found"
        )

    update_data = customer.dict(exclude_unset=True)
    update_data['updated_at'] = get_colombia_time()

    for key, value in update_data.items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    """Delete a customer by their ID."""
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail=f"Customer with id {customer_id} not found"
        )
    db.delete(db_customer)
    db.commit()
    return {"message" : f"Customer with id {customer_id} deleted successfully",
            "id" : customer_id}
