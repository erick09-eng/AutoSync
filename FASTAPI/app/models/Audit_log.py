# models/audit_log.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON

from db.database import Base


class AuditLog(Base):
    __tablename__ = "audit_log"

    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer) # ForeignKey("users.id")
    action = Column(String(255))
    table_name = Column(String(255))
    old_values = Column(JSON)
    new_values = Column(JSON)
    ip_address = Column(String(255))
    created_at = Column(DateTime)
    
