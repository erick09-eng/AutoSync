#schemas/audit_log.py
from pydantic import BaseModel
from datetime import datetime

class AuditLogBase(BaseModel):
    user_id : int
    action : str
    table_name : str
    old_values : Json
    new_values : Json
    ip_address : str
    created_at : datetime
    
class AuditLogCreate(AuditLogBase):
    pass

class AuditLogUpdate(AuditLogBase):
    pass

class AuditLogResponse(AuditLogBase):
    log_id : int

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v,
        }
        json_decoders = {
            datetime: lambda v: datetime.fromisoformat(v) if isinstance(v, str) else v,
        }
    