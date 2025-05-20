#app/services/audit_log_service.py
"""
This module contains the business logic for handling audit log-related operations.
It interacts with the database through the repository layer and handles
exceptions that may occur during these operations.
It provides functions to create, retrieve, and list audit log records.
"""
from repositories.audit_log_repository import (
    create_audit_log,
    get_audit_log,
    get_all_audit_logs,
)
from schemas.audit_log import AuditLogCreate, AuditLogResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

def create_audit_log_service(db: Session, audit_log: AuditLogCreate) -> AuditLogResponse:
    """
    Create a new audit log record in the database.
    """
    return create_audit_log(db, audit_log)

def get_audit_log_service(db: Session, audit_log_id: int) -> AuditLogResponse:
    """
    Retrieve an audit log record by its ID.
    """
    return get_audit_log(db, audit_log_id)

def get_all_audit_logs_service(db: Session) -> list[AuditLogResponse]:
    """
    Retrieve all audit log records.
    """
    return get_all_audit_logs(db)

def update_audit_log_service(db: Session,
                             audit_log_id: int,
                             audit_log: AuditLogCreate) -> AuditLogResponse:
    """
    Update an existing audit log record.
    """
    db_audit_log = get_audit_log(db, audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return create_audit_log(db, audit_log)

def delete_audit_log_service(db: Session, audit_log_id: int) -> AuditLogResponse:
    """
    Delete an audit log record by its ID.
    """
    db_audit_log = get_audit_log(db, audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit log not found")
    db.delete(db_audit_log)
    db.commit()
    return db_audit_log
