from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Roles(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(100), nullable=False)
    role_description = Column(Text, nullable=True)
