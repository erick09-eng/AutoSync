#services/audit_log_service.py
from sqlalchemy.orm import Session
from repositories.audit_log_repository import (
    create_audit_log, 
    get_audit_log, 
    get_all_audit_logs, 

)

from schemas.audit_log import AuditLogCreate, AuditLogResponse
from datetime import datetime

def create_audit_log_service(db: Session, audit_log: AuditLogCreate) -> AuditLogResponse:
    # TO DO Aquí se prondría la lógica de negocio (por ejemplo validar tipo de movimiento)
    return create_audit_log(db, audit_log)

def get_audit_log_service(db: Session, audit_log_id: int) -> AuditLogResponse:
    return get_audit_log(db, audit_log_id)

def get_all_audit_logs_service(db: Session) -> list[AuditLogResponse]:
    return get_all_audit_logs(db)



