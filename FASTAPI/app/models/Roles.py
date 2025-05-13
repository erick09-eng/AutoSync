"""
This module defines the Roles model for the database.

The Roles model represents user roles within the application.
"""
from sqlalchemy import Column, Integer, String, Text
from db.database import Base


class Roles(Base):
    """
    Represents a user role in the database.

    Attributes:
        role_id: The primary key for the role.
        role_name: The name of the role.
        role_description: A description of the role.
    """
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(100), nullable=False)
    role_description = Column(Text, nullable=True)
