# db/session.py
"""Database session management for FastAPI application.
This module provides a generator function to create and manage database sessions.
"""
#pylint: disable=invalid-name
from db.database import SessionLocal

def get_db():
    """Generator function to get a database session.
    This function creates a new database session and yields it.
    After the operation, it closes the session.
    Yields:
        Session: A SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
