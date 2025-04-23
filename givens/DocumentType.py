from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class DocumentType(Base):
    __tablename__ = "document_types"

    document_type_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
