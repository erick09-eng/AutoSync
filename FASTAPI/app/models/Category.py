from sqlalchemy import Column, Integer, String, ForeignKey, Text
from db.database import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parent_category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
