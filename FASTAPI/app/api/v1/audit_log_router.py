#app/api/v1/audit_log_router.py
"""FastAPI router for audit logs."""
from services.audit_log_service import (
    create_audit_log_service,
    get_audit_log_service,
    get_all_audit_logs_service,
    update_audit_log_service,
    delete_audit_log_service,
)

from schemas.audit_log import AuditLogCreate, AuditLogResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()
@router.post("/", response_model=AuditLogResponse)
def create_audit_log(audit_log: AuditLogCreate, db: Session = Depends(get_db)):
    """Create a new audit log."""
    return create_audit_log_service(db, audit_log)

@router.get("/{audit_log_id}", response_model=AuditLogResponse)
def get_audit_log(audit_log_id: int, db: Session = Depends(get_db)):
    """Get an audit log by ID."""
    db_audit_log = get_audit_log_service(db, audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return db_audit_log

@router.get("/", response_model=list[AuditLogResponse])
def get_all_audit_logs(db: Session = Depends(get_db)):
    """Get all audit logs."""
    return get_all_audit_logs_service(db)

@router.put("/{audit_log_id}", response_model=AuditLogResponse)
def update_audit_log(
    audit_log_id: int,
    audit_log: AuditLogCreate,
    db: Session = Depends(get_db)
):
    """Update an audit log by ID."""
    db_audit_log = update_audit_log_service(db, audit_log_id, audit_log)
    if not db_audit_log:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return db_audit_log

@router.delete("/{audit_log_id}", response_model=AuditLogResponse)
def delete_audit_log(audit_log_id: int, db: Session = Depends(get_db)):
    """Delete an audit log by ID."""
    db_audit_log = delete_audit_log_service(db, audit_log_id)
    if not db_audit_log:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return db_audit_log
