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
MYSQL_USER = os.getenv("MYSQL_USER", "")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "")
MYSQL_DB = os.getenv("MYSQL_DB", "")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
print(f"Connecting to database at {DATABASE_URL}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
