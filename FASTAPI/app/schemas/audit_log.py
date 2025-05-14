#schemas/audit_log.py
""" Schemas for audit logs """
from datetime import datetime
from pydantic import BaseModel, Json


class AuditLogBase(BaseModel):
    """ Base schema for audit logs """
    user_id : int
    action : str
    table_name : str
    old_values : Json
    new_values : Json
    ip_address : str
    created_at : datetime
    
class AuditLogCreate(AuditLogBase):
    """ Schema for creating an audit log """

class AuditLogUpdate(AuditLogBase):
    """ Schema for updating an audit log """

class AuditLogResponse(AuditLogBase):
    """ Schema for response of audit log """
    log_id : int

    class Config:
        """ ORM mode to convert SQLAlchemy models to Pydantic models """
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v,
        }
        json_decoders = {
            datetime: lambda v: datetime.fromisoformat(v) if isinstance(v, str) else v,
        }
