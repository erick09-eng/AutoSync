from repositories import RolesRepository
from schemas import RolesSchemas

def create_role(db: Session, role: RolesCreate):
    return RolesRepository.create_role(db, role)

def get_role(db: Session, role_id: int):
    return RolesRepository.get_role(db, role_id)

def get_all_roles(db: Session):
    return RolesRepository.get_all_roles(db)

def update_role(db: Session, role_id: int, role: RolesCreate):
    return RolesRepository.update_role(db, role_id, role)

def delete_role(db: Session, role_id: int):
    return RolesRepository.delete_role(db, role_id)
