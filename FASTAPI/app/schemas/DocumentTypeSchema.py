from pydantic import BaseModel
from typing import Optional

class DocumentTypeBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None

class DocumentTypeCreate(DocumentTypeBase):
    pass

class DocumentTypeUpdate(DocumentTypeBase):
    pass

class DocumentTypeResponse(DocumentTypeBase):
    document_type_id: int

    class Config:
        from_attributes = True
