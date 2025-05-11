#app/repositories/audit_log_repository.py
""" 
Audit Log Repository
This module contains functions to interact with the Audit Log database table.
It provides functions to create, read, and filter audit logs.
"""
from datetime import datetime
from models.audit_log import AuditLog
from schemas.audit_log import AuditLogCreate
from sqlalchemy.orm import Session

def create_audit_log(db: Session, audit_log: AuditLogCreate):
    """Create a new audit log entry in the database.
    Args:
        db (Session): The database session.
        audit_log (AuditLogCreate): The audit log entry to create.
    Returns:
        AuditLog: The created audit log entry.
    """
    # Convert the Pydantic model to a SQLAlchemy model
    db_audit_log = AuditLog(**audit_log.dict())
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)
    return db_audit_log

def get_audit_log(db: Session, audit_log_id: int):
    """Get an audit log entry by its ID.
    Args:
        db (Session): The database session.
        audit_log_id (int): The ID of the audit log entry to retrieve.
    Returns:
        AuditLog: The audit log entry with the specified ID.
    """
    # Query the database for the audit log entry with the specified ID
    # and return it.
    return db.query(AuditLog).filter(AuditLog.id == audit_log_id).first()

def get_all_audit_logs(db: Session):
    """Get all audit log entries.
    Query the database for all audit log entries and return them.
    This function is useful for retrieving all audit logs for display or analysis.
    in the application.
    It can be used in the admin panel or for auditing purposes.
    The function returns a list of AuditLog objects.
    Args:
        db (Session): The database session.
    Returns:
        list: A list of all audit log entries.
    """
    return db.query(AuditLog).all()

def get_audit_logs_by_date(db: Session, date: datetime):
    """Get audit log entries by date.
    Query the database for audit log entries with the specified date
    and return them.
    This function is useful for filtering audit logs by date.
    It can be used in the admin panel or for auditing purposes.
    The function returns a list of AuditLog objects.
    The date should be in the format YYYY-MM-DD.
    Example: 2023-10-01
    Args:
        db (Session): The database session.
        date (datetime): The date to filter audit logs by.
    Returns:
        list: A list of audit log entries that match the specified date.
    """
    return db.query(AuditLog).filter(AuditLog.date == date).all()
