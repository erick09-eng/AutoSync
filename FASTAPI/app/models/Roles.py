"""Roles model module.

This module contains the SQLAlchemy ORM model for roles.

Classes:
    Roles: Represents a user role.

"""

from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Roles(Base):
    """Represents a user role.

    Attributes:
        role_id (int): Primary key for the role.
        role_name (str): Name of the role.
        role_description (str): Description of the role.
    """

    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(100), nullable=False)
    role_description = Column(Text, nullable=True)
