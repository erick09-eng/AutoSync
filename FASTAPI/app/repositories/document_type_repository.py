#app/repositories/document_type_repository.py
"""DocumentType repository module 
This module contains the repository functions for document types.
"""

from models.document_type import DocumentType
from schemas.document_type_schema import DocumentTypeCreate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_document_type(db: Session, document_type: DocumentTypeCreate):
    """Create a new document type in the database."""
    db_document_type = DocumentType(**document_type.dict())
    db.add(db_document_type)
    db.commit()
    db.refresh(db_document_type)
    return db_document_type

def get_document_type(db: Session, document_type_id: int):
    """Get a document type by its ID."""
    return db.query(DocumentType).filter(DocumentType.document_type_id == document_type_id).first()

def get_all_document_types(db: Session):
    """Get all document types."""
    return db.query(DocumentType).all()

def update_document_type(db: Session, document_type_id: int,
                         document_type: DocumentTypeCreate):
    """Update an existing document type."""
    db_document_type = get_document_type(db, document_type_id)
    if not db_document_type:
        raise HTTPException(
            status_code=404,  # type: ignore
            detail="Document type with id {document_type_id} not found" # type: ignore
            )

    # update the document type
    for key, value in document_type.dict().items():
        setattr(db_document_type, key, value)

    db.commit()
    db.refresh(db_document_type)  # refresh the instance to get the updated values
    return db_document_type  # return the updated instance
    
def delete_document_type(db: Session, document_type_id: int):
    """Delete a document type."""
    db_document_type = get_document_type(db, document_type_id)

    if not db_document_type:
        raise HTTPException(
            status_code=404,  
            detail=f"Document type with id {document_type_id} not found" 
        )
    db.delete(db_document_type)
    db.commit()
    return {
        "message": f"Documento con id {document_type_id} eliminado correctamente",
        "id": document_type_id
    }
