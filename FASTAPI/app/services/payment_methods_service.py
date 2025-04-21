#services/payment_methods_service.py
from sqlalchemy.orm import Session
from repositories.payment_methods_repository import create_payment_method, get_payment_method, get_all_payment_methods
from schemas.payment_methods import PaymentMethodCreate

def create_payment_method_service(db: Session, payment_method: PaymentMethodCreate):
    return create_payment_method(db, payment_method)


def get_payment_method_service(db: Session, payment_method_id: int):
    return get_payment_method(db, payment_method_id)

def get_all_payment_methods_service(db: Session):
    return get_all_payment_methods(db)


