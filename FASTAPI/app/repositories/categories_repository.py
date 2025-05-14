from sqlalchemy.orm import Session

from models.category import Category as Categories
from schemas.CategorySchema import CategoryCreate as CategoriesCreate

def create_category(db: Session, category: CategoriesCreate):
    db_category = Categories(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Categories).filter(Categories.id == category_id).first()

def get_all_categories(db: Session):
    return db.query(Categories).all()

def update_category(db: Session, category_id: int, category: CategoriesCreate):
    db_category = get_category(db, category_id)
    if db_category:
        for key, value in category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        
def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()