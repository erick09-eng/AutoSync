#repositories/payments_repository.py
from sqlalchemy.orm import Session
from models import payments as Payments
from schemas.payments import PaymentCreate, PaymentResponse

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payments(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db: Session, payment_id: int):
    return db.query(Payments).filter(Payments.payment_id == payment_id).first()


def get_all_payments(db: Session):
    return db.query(Payments).all()


def update_payment(db: Session, payment_id: int, payment: PaymentCreate):
    db_payment = db.query(Payments).filter(Payments.payment_id == payment_id).first()
    if db_payment:
        for key, value in payment.dict().items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment


def delete_payment(db: Session, payment_id: int):
    db_payment = db.query(Payments).filter(Payments.payment_id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment


