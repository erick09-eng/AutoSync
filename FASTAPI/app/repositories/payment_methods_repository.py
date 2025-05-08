#repositories/payment_methods_repository.py
from sqlalchemy.orm import Session
from models.Payment_methods import PaymentMethod
from schemas.payment_methods import PaymentMethodCreate

def create_payment_method(db: Session, payment_method: PaymentMethodCreate):
    db_payment_method = PaymentMethod(**payment_method.dict())
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method

def get_payment_method(db: Session, payment_method_id: int):
    return db.query(PaymentMethod).filter(PaymentMethod.payment_method_id == payment_method_id).first()

def get_all_payment_methods(db: Session):
    return db.query(PaymentMethod).all()

def update_payment_method(db: Session, payment_method_id: int, payment_method: PaymentMethodCreate):
    db_payment_method = db.query(PaymentMethod).filter(PaymentMethod.payment_method_id == payment_method_id).first()
    if db_payment_method:
        for key, value in payment_method.dict().items():
            setattr(db_payment_method, key, value)
        db.commit()
        db.refresh(db_payment_method)
    return db_payment_method

def delete_payment_method(db: Session, payment_method_id: int):
    db_payment_method = db.query(PaymentMethod).filter(PaymentMethod.payment_method_id == payment_method_id).first()
    if db_payment_method:
        db.delete(db_payment_method)
        db.commit()
    return db_payment_method

