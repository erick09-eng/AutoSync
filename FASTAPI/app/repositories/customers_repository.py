"""Repository for managing customers in the database."""
from models import customers as Customer
from schemas.customer_schema import CustomerCreate
from sqlalchemy.orm import Session


def create_customer(db: Session, customer: CustomerCreate):
    """Create a new customer in the database."""
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customer(db: Session, customer_id: int):
    """Retrieve a customer by their ID."""
    return db.query(Customer).filter(Customer.id == customer_id).first()


def get_all_customers(db: Session):
    """Retrieve all customers."""
    return db.query(Customer).all()


def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
    """Update an existing customer in the database."""
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in customer.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int):
    """Delete a customer by their ID."""
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return True
    return False
