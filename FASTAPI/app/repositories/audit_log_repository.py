#repositories/audit_log_repository.py
from sqlalchemy.orm import Session
from models.audit_log import AuditLog
from schemas.audit_log import AuditLogCreate, AuditLogResponse
from datetime import datetime

def create_audit_log(db: Session, audit_log: AuditLogCreate):
    db_audit_log = AuditLog(**audit_log.dict())
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)
    return db_audit_log

def get_audit_log(db: Session, audit_log_id: int):
    return db.query(AuditLog).filter(AuditLog.id == audit_log_id).first()

def get_all_audit_logs(db: Session):
    return db.query(AuditLog).all()

def get_audit_logs_by_date(db: Session, date: datetime):
    return db.query(AuditLog).filter(AuditLog.date == date).all()

