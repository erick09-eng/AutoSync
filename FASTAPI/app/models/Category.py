"""
Module defining the Category model for the database.

This module contains the definition of the Category class which represents
product categories in the system, including hierarchical relationships.
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from db.database import Base


class Category(Base):
    """
    Database model for product categories.

    Defines the SQLAlchemy Category model representing product classification
    in the system, with support for parent-child category relationships.
    """
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parent_category_id = Column(
        Integer,
        ForeignKey("categories.category_id"),
        nullable=True
    )
