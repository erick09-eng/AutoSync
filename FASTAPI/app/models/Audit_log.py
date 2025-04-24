# models/Audit_Log.py
from sqlalchemy import Column, Integer, String, Json, Timestamp
from db.database import Base


class Audit_log(Base):
    __tablename__ = "audit_log"

    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer) # ForeignKey("users.id")
    action = Column(String(255))
    table_name = Column(String(255))
    old_values = Column(Json)
    new_values = Column(Json)
    ip_address = Column(String(255))
    created_at = Column(Timestamp)
    
