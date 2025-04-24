from sqlalchemy import Column, Integer, Float, String, DateTime
from db.database import Base

class Sale(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    document_type_id = Column(Integer)  # ForeignKey("document_types.document_type_id")
    serial_number = Column(String(100), nullable=False)
    customer_id = Column(Integer)       # ForeignKey("customers.customer_id")
    user_id = Column(Integer)           # ForeignKey("users.user_id")
    subtotal = Column(Float, nullable=False)
    tax_amount = Column(Float, nullable=False)
    discount_amount = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)
    payment_method = Column(String(50), default="cash")
    status = Column(String(50), default="completed")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
