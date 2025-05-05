from sqlalchemy.orm import Session

from models.Roles import Roles
from schemas.RolesSchema import RoleCreate, RoleResponse

def create_role(db: Session, role: RoleCreate):
    db_role = Roles(**role.dict())
    db.add(db_role)
    db.commit()

def get_role(db: Session, role_id: int):
    return db.query(Roles).filter(Roles.id == role_id).first()

def get_all_roles(db: Session):
    return db.query(Roles).all()

def update_role(db: Session, role_id: int, role: RoleCreate):
    db_role = get_role(db, role_id)
    if db_role:
        for key, value in role.dict().items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role

def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
        return True
    