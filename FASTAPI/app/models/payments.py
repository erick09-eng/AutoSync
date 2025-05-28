# app/models/payments.py
"""Payments model module.

This module contains the SQLAlchemy ORM model for payments.

Classes:
    Payments: Represents a payment record.

"""

from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.types import DateTime

from db.database import Base

# pylint: disable=too-few-public-methods
class Payments(Base):
    """Represents a payment.

    Attributes:
        payment_id (int): Primary key for the payment.
        sale_id (int): Foreign key to the sales table.
        payment_method_id (int): Foreign key to the payment methods table.
        amount (float): Amount paid.
        transaction_code (str): Transaction code or reference number.
        payment_date (datetime): Date of payment (YYYY-MM-DD).
        status (str): Status of the payment (pending, completed, failed).
    """

    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer,ForeignKey("sales.sale_id"), index=True)  # Foreign key to sales table
    payment_method_id = Column(Integer,
                               ForeignKey("payment_methods.payment_method_id"),
                               index=True)  # Foreign key to payment methods table
    amount = Column(Double)  # Amount paid
    transaction_code = Column(String(255))  # Transaction code or reference number
    payment_date = Column(DateTime)  # Date of payment (YYYY-MM-DD)
    status = Column(String(255))  # Status of the payment (pending, completed, failed)
