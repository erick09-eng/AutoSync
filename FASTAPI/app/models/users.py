# app/models/users.py
"""Users model module.
This module contains the SQLAlchemy ORM model for users.
Classes:
    User: Represents a user.
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from db.database import Base

class User(Base):
    """Represents a user.

    Attributes:
        user_id (int): Primary key for the user.
        username (str): Unique username.
        password_hash (str): Hashed password.
        full_name (str): Full name of the user.
        email (str): Email address.
        role_id (int): Foreign key to the roles table.
        is_active (bool): Indicates if the user is active.
        created_at (datetime): Timestamp when the user was created.
        updated_at (datetime): Timestamp when the user was last updated.
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
