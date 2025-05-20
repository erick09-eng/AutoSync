#api/v1/roles_router.py
"""FastAPI router for managing user roles."""
from services.roles_service import (
    create_role,
    get_role,
    get_all_roles,
    update_role,
    delete_role,
)
from schemas.roles_schema import RoleCreate, RoleResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=RoleResponse)
def create(role: RoleCreate, db: Session = Depends(get_db)):
    """Create a new role."""
    return create_role(db, role)

@router.get("/{role_id}", response_model=RoleResponse)
def read(role_id: int, db: Session = Depends(get_db)):
    """Get a role by its ID."""
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.get("/", response_model=list[RoleResponse])
def list_all(db: Session = Depends(get_db)):
    """Get a list of all roles."""
    return get_all_roles(db)

@router.put("/{role_id}", response_model=RoleResponse)
def update(role_id: int, role: RoleCreate,
           db: Session = Depends(get_db)):
    """Update an existing role."""
    return update_role(db, role_id, role)

@router.delete("/{role_id}")
def delete(role_id: int, db: Session = Depends(get_db)):
    """Delete a role by its ID."""
    return delete_role(db, role_id)
