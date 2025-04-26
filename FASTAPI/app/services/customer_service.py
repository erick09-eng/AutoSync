from repositories.roles_repository import RolesRepository
from schemas.roles_schema import RolesCreate

def create_user(db: Session, user: UserCreate):
    return RolesRepository.create(db, user)

def get_user(db: Session, user_id: int):
    return RolesRepository.get_by_id(db, user_id) 

def get_all_users(db: Session):
    return RolesRepository.get_all(db)

def update_user(db: Session, user_id: int, user: UserCreate):
    return RolesRepository.update(db, user_id, user)

def delete_user(db: Session, user_id: int):
    return RolesRepository.delete(db, user_id)