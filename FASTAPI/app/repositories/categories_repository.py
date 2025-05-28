# app/repositories/categories_repository.py
"""Repository for managing categories in the database."""
from models.category import Category
from schemas.category_schema import CategoryCreate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_category(db: Session, category: CategoryCreate):
    """Create a new category in the database."""
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    """Retrieve a category by its ID."""
    return db.query(Category).filter(Category.category_id == category_id).first()

def get_all_categories(db: Session):
    """Retrieve all categories."""
    return db.query(Category).all()

def update_category(db: Session, category_id: int, category: CategoryCreate):
    """Update an existing category by its ID."""
    db_category = get_category(db, category_id)
    if not db_category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {category_id} not found"
        )
    # Update the category attributes
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    """Delete a category by its ID."""
    db_category = get_category(db, category_id)
    if not db_category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {category_id} not found"
        )
    db.delete(db_category)
    db.commit()
    return {
        "message": f"Category with id {category_id} deleted successfully",
        "id": category_id
    }
