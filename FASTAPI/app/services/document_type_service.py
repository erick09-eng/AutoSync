#app/services/document_type_service.py
"""DocumentType service module.
This module contains the service functions for document types.
Functions:
    create_document_type: Create a new document type.
    get_document_type: Get a document type by its ID.
    get_all_document_types: Get all document types.
    update_document_type: Update an existing document type.
    delete_document_type: Delete a document type.
"""

from repositories import document_type_repository as DocumentTypeRepository
from schemas.document_type_schema import DocumentTypeCreate, DocumentTypeUpdate
from sqlalchemy.orm import Session

def create_document_type(db: Session,
                         document_type: DocumentTypeCreate):
    """Create a new document type."""
    return DocumentTypeRepository.create_document_type(db, document_type)

def get_document_type(db: Session, document_type_id: int):
    """Get a document type by its ID."""
    return DocumentTypeRepository.get_document_type(db, document_type_id)

def get_all_document_types(db: Session):
    """Get all document types."""
    return DocumentTypeRepository.get_all_document_types(db)

def update_document_type(db: Session, document_type_id: int,
                         document_type: DocumentTypeUpdate):
    """Update an existing document type."""
    return DocumentTypeRepository.update_document_type(db, document_type_id, document_type)

def delete_document_type(db: Session, document_type_id: int):
    """Delete a document type."""
    return DocumentTypeRepository.delete_document_type(db, document_type_id)
