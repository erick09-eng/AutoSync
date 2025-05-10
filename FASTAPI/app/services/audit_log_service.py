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
from sqlalchemy.orm import Session

def create_audit_log_service(db: Session, audit_log: AuditLogCreate) -> AuditLogResponse:
    """
    Create a new audit log record in the database.
    """
    # TO DO Aquí se prondría la lógica de negocio (por ejemplo validar tipo de movimiento)
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
