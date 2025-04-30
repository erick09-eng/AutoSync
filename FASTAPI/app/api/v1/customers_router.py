from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.customers_service import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)
from schemas.customers_schema import CustomersCreate, CustomersResponse

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomersResponse)
def create(customer: CustomersCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/{customer_id}", response_model=CustomersResponse)
def read(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=list[CustomersResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_customers(db)

@router.put("/{customer_id}", response_model=CustomersResponse)
def update(customer_id: int, customer: CustomersCreate, db: Session = Depends(get_db)):
    return update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    return delete_customer(db, customer_id)
