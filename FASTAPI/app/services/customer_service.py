from repositories.customers_repository import CustomersRepository
from schemas.customers_schema import CustomersCreate
from sqlalchemy.orm import Session

def create_customer(db: Session, customer: CustomersCreate):
    return CustomersRepository.create(db, customer)

def get_customer(db: Session, customer_id: int):
    return CustomersRepository.get_by_id(db, customer_id)

def get_all_customers(db: Session):
    return CustomersRepository.get_all(db)

def update_customer(db: Session, customer_id: int, customer: CustomersCreate):
    return CustomersRepository.update(db, customer_id, customer)

def delete_customer(db: Session, customer_id: int):
    return CustomersRepository.delete(db, customer_id)