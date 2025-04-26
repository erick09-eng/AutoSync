from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.category_service import (
    create_category,
    get_category,
    get_all_categories,
    update_category,
    delete_category,
)
from schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryResponse)
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/{category_id}", response_model=CategoryResponse)
def read(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.get("/", response_model=list[CategoryResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_categories(db)

@router.put("/{category_id}", response_model=CategoryResponse)
def update(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    return update_category(db, category_id, category)

@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)
