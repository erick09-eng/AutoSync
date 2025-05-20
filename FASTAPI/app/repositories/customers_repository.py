#app/repositories/customers_repository.py
"""Repository for managing users in the database."""
from models import Users as User
from schemas.UserSchema import UserCreate
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    """Create a new user in the database."""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    """Retrieve a user by its ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    """Retrieve all users.""" 
    return db.query(User).all()

def update_user(db: Session, user_id: int, user: UserCreate):
    """Update an existing user in the database."""
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()

def delete_user(db: Session, user_id: int):
    """Delete a user by its ID."""
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
