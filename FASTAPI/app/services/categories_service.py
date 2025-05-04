from repositories import categories_repository as CategoriesRepository
from sqlalchemy.orm import Session
from schemas.CategorySchema import CategoryCreate as CategoriesCreate, CategoryResponse as CategoryResponse

def create_category(db: Session, category: CategoriesCreate):
    return CategoriesRepository.create_category(db, category)

def get_category(db: Session, category_id: int):
    return CategoriesRepository.get_category(db, category_id)

def get_all_categories(db: Session):
    return CategoriesRepository.get_all_categories(db)

def update_category(db: Session, category_id: int, category: CategoriesCreate):
    return CategoriesRepository.update_category(db, category_id, category)

def delete_category(db: Session, category_id: int):
    return CategoriesRepository.delete_category(db, category_id)