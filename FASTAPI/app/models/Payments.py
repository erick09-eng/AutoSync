# models/payments.py
""""
This module defines the Payments model, which represents the payments made
in the system. It includes attributes such as payment ID, sale ID, payment method
ID, amount, transaction code, payment date, and status.
"""
from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.types import DateTime

from db.database import Base

# pylint: disable=too-few-public-methods
class Payments(Base):
    """
    Represents a payment in the database.
    Attributes:
        payment_id (int): The unique identifier for the payment.
        sale_id (int): The ID of the sale associated with the payment.
        payment_method_id (int): The ID of the payment method used.
        amount (float): The amount paid.
        transaction_code (str): The transaction code or reference number.
        payment_date (datetime): The date of payment.
        status (str): The status of the payment (e.g., pending, completed, failed).
    """
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, index=True)  # Foreign key to sales table
    payment_method_id = Column(Integer, index=True)  # Foreign key to payment methods table
    amount = Column(Double)  # Amount paid
    transaction_code = Column(String)  # Transaction code or reference number
    payment_date = Column(DateTime)  # Date of payment (YYYY-MM-DD)
    status = Column(String)  # Status of the payment (pending, completed, failed)
