"""
Module defining document types (e.g., ID cards, passports, etc.).

Contains the DocumentType model for identity document classification in database.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)
from db.database import Base


class DocumentType(Base):
    """
    Represents types of identity documents in the system.

    Attributes:
        document_type_id (int): Primary key identifier
        code (str): Unique document type code (e.g., "PASSPORT")
        name (str): Full document type name (e.g., "Passport")
        description (str): Optional detailed description
    """
    __tablename__ = "document_types"

    document_type_id = Column(Integer, primary_key=True, index=True) #primary key
    code = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
