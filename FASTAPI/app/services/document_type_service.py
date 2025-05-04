from sqlalchemy.orm import Session
from repositories import document_type_repository as DocumentTypeRepository
from schemas.DocumentTypeSchema import DocumentTypeCreate, DocumentTypeUpdate

def create_document_type(db: Session, document_type: DocumentTypeCreate):
    return DocumentTypeRepository.create_document_type(db, document_type)

def get_document_type(db: Session, document_type_id: int):
    return DocumentTypeRepository.get_document_type(db, document_type_id)

def get_all_document_types(db: Session):
    return DocumentTypeRepository.get_all_document_types(db)

def update_document_type(db: Session, document_type_id: int, document_type: DocumentTypeUpdate):
    return DocumentTypeRepository.update_document_type(db, document_type_id, document_type)

def delete_document_type(db: Session, document_type_id: int):
    return DocumentTypeRepository.delete_document_type(db, document_type_id)