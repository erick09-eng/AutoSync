"""Audit_log model module.

This module contains the SQLAlchemy ORM model for audit logs.

Classes:
    AuditLog: Represents an audit log record.

"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSON

from db.database import Base


class AuditLog(Base):
    """Represents an audit log entry.

    Attributes:
        log_id (int): Primary key for the audit log.
        user_id (int): Foreign key to the users table.
        action (str): Action performed.
        table_name (str): Name of the table affected.
        old_values (JSON): Previous values before the change.
        new_values (JSON): New values after the change.
        ip_address (str): IP address from where the action was performed.
        created_at (datetime): Timestamp when the log was created.
    """

    __tablename__ = "audit_log"

    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id")) # ForeignKey("users.id")
    action = Column(String(255))
    table_name = Column(String(255))
    old_values = Column(JSON)
    new_values = Column(JSON)
    ip_address = Column(String(255))
    created_at = Column(DateTime)
    
    
