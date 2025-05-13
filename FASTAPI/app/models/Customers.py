"""
This module contains the SQLAlchemy model definition for Customers.

The Customers model represents customer information in the database,
including personal details, contact information, and activity status.
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.database import Base


class Customers(Base):
    __tablename__ = "customers"
    """
    This module defines the Customers model for the database.
    The Customers model represents customer information in the application.
    """
    customer_id = Column(Integer, primary_key=True, index=True)
    tax_id = Column(String(100), nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
