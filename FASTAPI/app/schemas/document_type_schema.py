#app/schemas/DocumentTypeSchema.py
# pylint: disable=too-few-public-methods
"""DocumentType schema module.
This module contains the Pydantic schemas for document types.
Schemas:
    DocumentTypeBase: Base schema for document types.
    DocumentTypeCreate: Schema for creating a new document type.
    DocumentTypeUpdate: Schema for updating an existing document type.
    DocumentTypeResponse: Schema for returning a document type response.
"""
from typing import Optional
from pydantic import BaseModel

class DocumentTypeBase(BaseModel):
    """Base schema for document types.
    """
    code: str
    name: str
    description: Optional[str] = None

class DocumentTypeCreate(DocumentTypeBase):
    """Schema for creating a new document type.
    """

class DocumentTypeUpdate(DocumentTypeBase):
    """Schema for updating an existing document type.
    """

class DocumentTypeResponse(DocumentTypeBase):
    """Schema for returning a document type response.
    """
    document_type_id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True
