# models/item.py
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    on_offer = Column(Boolean, default=True)
