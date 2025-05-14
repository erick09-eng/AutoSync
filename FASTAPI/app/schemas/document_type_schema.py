"""FastAPI schema for Sale model"""
from typing import Optional
from pydantic import BaseModel


class DocumentTypeBase(BaseModel):
    """ Base schema for DocumentType model"""
    code: str
    name: str
    description: Optional[str] = None


class DocumentTypeCreate(DocumentTypeBase):
    """Schema for creating new DocumentType records"""
    pass


class DocumentTypeUpdate(DocumentTypeBase):
    """Schema for updating existing DocumentType records"""
    pass


class DocumentTypeResponse(DocumentTypeBase):
    """Schema for DocumentType response including ID"""
    document_type_id: int

    class Config: # pylint: disable=too-few-public-methods
        """Configuration for Pydantic models"""
        from_attributes = True
