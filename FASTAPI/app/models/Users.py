"""
This module defines the User model for the database.

The User model represents user information in the application.
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    role_id = Column(Integer)  # ForeignKey("roles.role_id")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
