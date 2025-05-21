#app/services/roles_service.py
"""FastAPI service for managing user roles."""
from repositories import roles_repository
from schemas.roles_schema import RoleCreate
from sqlalchemy.orm import Session

def create_role(db: Session, role: RoleCreate):
    """Create a new role."""
    return roles_repository.create_role(db, role)

def get_role(db: Session, role_id: int):
    """Get a role by its ID."""
    return roles_repository.get_role(db, role_id)

def get_all_roles(db: Session):
    """Get a list of all roles."""
    return roles_repository.get_all_roles(db)

def update_role(db: Session, role_id: int, role: RoleCreate):
    """Update an existing role."""
    return roles_repository.update_role(db, role_id, role)

def delete_role(db: Session, role_id: int):
    """Delete a role by its ID."""
    return roles_repository.delete_role(db, role_id)
