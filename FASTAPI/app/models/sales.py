# app/models/sales.py
"""Sales model module.

This module contains the SQLAlchemy ORM model for sales.

Classes:
    Sale: Represents a sale record.

"""

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from db.database import Base

class Sale(Base):
    """Represents a sale.

    Attributes:
        sale_id (int): Primary key for the sale.
        document_type_id (int): Foreign key to the document types table.
        serial_number (str): Serial number of the sale.
        customer_id (int): Foreign key to the customers table.
        user_id (int): Foreign key to the users table.
        subtotal (float): Subtotal amount.
        tax_amount (float): Tax amount.
        discount_amount (float): Discount amount.
        total_amount (float): Total amount.
        payment_method (str): Payment method used.
        status (str): Status of the sale.
        created_at (datetime): Timestamp when the sale was created.
        updated_at (datetime): Timestamp when the sale was last updated.
    """

    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    document_type_id = Column(Integer,
                              ForeignKey("document_types.document_type_id"),
                              nullable=False)  # ForeignKey("document_types.document_type_id")
    serial_number = Column(String(100), nullable=False)
    customer_id = Column(Integer,
                         ForeignKey("customers.customer_id"),
                         nullable=False)       # ForeignKey("customers.customer_id")
    user_id = Column(Integer,
                     ForeignKey("users.user_id"),
                     nullable=False)           # ForeignKey("users.user_id")
    subtotal = Column(Float, nullable=False)
    tax_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)
    payment_method = Column(Integer,
                            ForeignKey("payment_methods.payment_method_id"),
                            nullable=False)
    status = Column(String(50), default="completed")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
