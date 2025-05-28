"""Database connection and session management for FastAPI application.
This module sets up the connection to the MySQL database using SQLAlchemy.
It creates a session local class for database interactions and a base class for
ORM models.
"""
# pylint: disable=invalid-name
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Removed dotenv loading from here, assuming it is loaded in main.py

# Configurar conexión con MySQL
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "")
DB_NAME = os.getenv("DB_NAME", "")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
print(f"Connecting to database at {DATABASE_URL}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
