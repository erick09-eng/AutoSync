#app/repositories/roles_repository.py
"""Roles Repository Module
This module contains functions to interact with the Roles table in the database.
It includes functions to create, read, update, and delete roles.
"""
from models.roles import Roles
from schemas.roles_schema import RoleCreate
from sqlalchemy.orm import Session

def create_role(db: Session, role: RoleCreate):
    """Create a new role in the database."""
    db_role = Roles(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    """Get a role by ID."""
    return db.query(Roles).filter(Roles.role_id == role_id).first()

def get_all_roles(db: Session):
    """Get all roles."""
    return db.query(Roles).all()

def update_role(db: Session, role_id: int, role: RoleCreate):
    """Update an existing role."""
    db_role = get_role(db, role_id)
    if db_role:
        for key, value in role.dict().items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role

def delete_role(db: Session, role_id: int):
    """Delete a role by ID."""
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
        return True
