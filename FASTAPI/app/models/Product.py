"""Product model module.

This module contains the SQLAlchemy ORM model for products.

Classes:
    Product: Represents a product.

"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from db.database import Base

class Product(Base):
    """Represents a product.

    Attributes:
        product_id (int): Primary key for the product.
        sku (str): Stock keeping unit, unique identifier.
        name (str): Name of the product.
        description (str): Description of the product.
        category_id (int): Foreign key to the categories table.
        unit_price (float): Unit price of the product.
        cost_price (float): Cost price of the product.
        current_stock (int): Current stock quantity.
        min_stock (int): Minimum stock threshold.
        on_offer (bool): Indicates if the product is on offer.
        offer_price (float): Offer price if on offer.
        is_active (bool): Indicates if the product is active.
        created_at (datetime): Timestamp when the product was created.
        updated_at (datetime): Timestamp when the product was last updated.
    """

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, nullable=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    unit_price = Column(Float, nullable=False)
    cost_price = Column(Float, nullable=True)
    current_stock = Column(Integer)
    min_stock = Column(Integer)
    on_offer = Column(Boolean, default=False)
    offer_price = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
