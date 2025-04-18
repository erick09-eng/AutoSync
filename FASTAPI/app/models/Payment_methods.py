# models/Payment_methods.py
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Payment_methods(Base):
    __tablename__ = "payment_methods"

    payment_method_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    requieres_authorization = Column(Boolean, default=False)

