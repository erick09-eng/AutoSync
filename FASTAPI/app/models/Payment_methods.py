# models/payment_methods.py
"""
This module defines the PaymentMethod model, which represents payment methods
in the database. It includes attributes such as name, description, and whether
authorization is required.
"""
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

# pylint: disable=too-few-public-methods
class PaymentMethod(Base):
    """Represents a payment method in the database.
    Attributes:
        payment_method_id (int): The unique identifier for the payment method.
        name (str): The name of the payment method.
        description (str): A description of the payment method.
        requieres_authorization (bool): Indicates if authorization is required.
    """
    __tablename__ = "payment_methods"

    payment_method_id = Column(Integer, primary_key=True, index=True)
    payment_method_name = Column(String, index=True)
    description = Column(String, index=True)
    requieres_authorization = Column(Boolean, default=False)
