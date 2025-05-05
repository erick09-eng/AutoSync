from sqlalchemy.orm import Session

from models.DocumentType import DocumentType
from schemas.DocumentTypeSchema import DocumentTypeCreate, DocumentTypeResponse

def create_document_type(db: Session, document_type: DocumentTypeCreate):
    db_document_type = DocumentType(**document_type.dict())
    db.add(db_document_type)
    db.commit()
    db.refresh(db_document_type)
    return db_document_type

def get_document_type(db: Session, document_type_id: int):
    return db.query(DocumentType).filter(DocumentType.id == document_type_id).first()

def get_all_document_types(db: Session):
    return db.query(DocumentType).all()

def update_document_type(db: Session, document_type_id: int, document_type: DocumentTypeCreate):
    db_document_type = get_document_type(db, document_type_id)
    if db_document_type:
        for key, value in document_type.dict().items():
            setattr(db_document_type, key, value)
        db.commit()
        
def delete_document_type(db: Session, document_type_id: int):
    db_document_type = get_document_type(db, document_type_id)
    if db_document_type:
        db.delete(db_document_type)
        db.commit()
        