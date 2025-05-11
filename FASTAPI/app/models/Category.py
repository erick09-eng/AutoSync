"""Category model module.

This module contains the SQLAlchemy ORM model for categories.

Classes:
    Category: Represents a product category.

"""

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from db.database import Base

class Category(Base):
    """Represents a product category.

    Attributes:
        category_id (int): Primary key for the category.
        name (str): Name of the category.
        description (str): Description of the category.
        parent_category_id (int): Foreign key to the parent category.
    """

    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parent_category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
