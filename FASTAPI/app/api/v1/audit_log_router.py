#api/v1/audit_log_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.audit_log_service import (
    create_audit_log_service,
    get_audit_log_service,
    get_all_audit_logs_service,
)
from schemas.audit_log import AuditLogCreate, AuditLogResponse

router = APIRouter()

@router.post("/", response_model=AuditLogResponse)
def create_audit_log(audit_log: AuditLogCreate, db: Session = Depends(get_db)):
    return create_audit_log_service(db, audit_log)

@router.get("/{audit_log_id}", response_model=AuditLogResponse)
def read_audit_log(audit_log_id: int, db: Session = Depends(get_db)):
    db_audit_log = get_audit_log_service(db, audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return db_audit_log

@router.get("/", response_model=list[AuditLogResponse])
def list_audit_logs(db: Session = Depends(get_db)):
    return get_all_audit_logs_service(db)

# Add any additional endpoints or logic as needed
    