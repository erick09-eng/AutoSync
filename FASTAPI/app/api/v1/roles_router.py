from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.roles_service import (
    create_role,
    get_role,
    get_all_roles,
    update_role,
    delete_role,
)
from schemas.RolesSchema import RoleCreate, RoleResponse

router = APIRouter()

@router.post("/", response_model=RoleResponse)
def create(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/{role_id}", response_model=RoleResponse)
def read(role_id: int, db: Session = Depends(get_db)):
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.get("/", response_model=list[RoleResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_roles(db)

@router.put("/{role_id}", response_model=RoleResponse)
def update(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    return update_role(db, role_id, role)

@router.delete("/{role_id}")
def delete(role_id: int, db: Session = Depends(get_db)):
    return delete_role(db, role_id)
