# models/Payments.py
from sqlalchemy import Column, Integer, String, Boolean, Double, Datetime
from db.database import Base


class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, index=True)  # Foreign key to sales table
    payment_method_id = Column(Integer, index=True)  # Foreign key to payment methods table
    amount = Column(Double)  # Amount paid
    transaction_code = Column(String)  # Transaction code or reference number
    payment_date = Column(Datetime)  # Date of payment (YYYY-MM-DD)
    status = Column(String)  # Status of the payment (pending, completed, failed)

