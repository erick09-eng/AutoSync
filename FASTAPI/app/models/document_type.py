# app/models/document_type.py
"""DocumentType model module.

This module contains the SQLAlchemy ORM model for document types.

Classes:
    DocumentType: Represents a document type.

"""

from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class DocumentType(Base):
    """Represents a document type.

    Attributes:
        document_type_id (int): Primary key for the document type.
        code (str): Code of the document type.
        name (str): Name of the document type.
        description (str): Description of the document type.
    """

    __tablename__ = "document_types"

    document_type_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
