#app/api/v1/document_types_router.py
"""DocumentType API router module.
This module contains the FastAPI router for document types.
"""
from services.document_type_service import (
    create_document_type,
    get_document_type,
    get_all_document_types,
    update_document_type,
    delete_document_type,
)
from schemas.document_type_schema import ( DocumentTypeCreate,
DocumentTypeUpdate,
DocumentTypeResponse
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=DocumentTypeResponse)
def create(document_type: DocumentTypeCreate, db: Session = Depends(get_db)):
    """Create a new document type."""
    return create_document_type(db, document_type)

@router.get("/{document_type_id}", response_model=DocumentTypeResponse)
def read(document_type_id: int, db: Session = Depends(get_db)):
    """Get a document type by its ID."""
    db_document_type = get_document_type(db, document_type_id)
    if db_document_type is None:
        raise HTTPException(status_code=404, detail="Document type not found")
    return db_document_type

@router.get("/", response_model=list[DocumentTypeResponse])
def list_all(db: Session = Depends(get_db)):
    """Get all document types."""
    document_types = get_all_document_types(db)
    if not isinstance(document_types, list):
        raise HTTPException(500, "Unexpected response format")
    return document_types

@router.put("/{document_type_id}", response_model=DocumentTypeResponse)
def update(document_type_id: int, document_type: DocumentTypeUpdate,
           db: Session = Depends(get_db)):
    """Update an existing document type."""
    return update_document_type(db, document_type_id, document_type)

@router.delete("/{document_type_id}")
def delete(document_type_id: int, db: Session = Depends(get_db)):
    """Delete a document type."""
    return delete_document_type(db, document_type_id)
