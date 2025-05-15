#app/api/v1/categories_router.py
"""Category API router module.
This module contains the FastAPI router for category-related operations.
It provides endpoints for creating, reading, updating, and deleting categories.
"""
from services.categories_service import (
    create_category,
    get_category,
    get_all_categories,
    update_category,
    delete_category,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.category_schema import CategoryCreate, CategoryResponse

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    """Create a new category."""
    return create_category(db, category)

@router.get("/{category_id}", response_model=CategoryResponse)
def read(category_id: int, db: Session = Depends(get_db)):
    """Get a category by its ID."""
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.get("/", response_model=list[CategoryResponse])
def list_all(db: Session = Depends(get_db)):
    """Get all categories."""
    return get_all_categories(db)

@router.put("/{category_id}", response_model=CategoryResponse)
def update(category_id: int, category: CategoryCreate,
           db: Session = Depends(get_db)):
    """Update an existing category."""
    return update_category(db, category_id, category)

@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    """Delete a category."""
    return delete_category(db, category_id)
