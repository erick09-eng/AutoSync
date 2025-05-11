"""Customers model module.

This module contains the SQLAlchemy ORM model for customers.

Classes:
    Customers: Represents a customer.

"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.database import Base

class Customers(Base):
    """Represents a customer.

    Attributes:
        customer_id (int): Primary key for the customer.
        tax_id (str): Tax identification number.
        full_name (str): Full name of the customer.
        email (str): Email address.
        phone (str): Phone number.
        address (str): Address.
        is_active (bool): Indicates if the customer is active.
        created_at (datetime): Timestamp when the customer was created.
        updated_at (datetime): Timestamp when the customer was last updated.
    """

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    tax_id = Column(String(100), nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
