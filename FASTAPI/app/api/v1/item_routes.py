# api/v1/item_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.item import ItemCreate, ItemResponse
from services.item_service import create_new_item, fetch_item
from db.session import get_db

router = APIRouter()


@router.post("/", response_model=ItemResponse)
def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    return create_new_item(db, item)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item_route(item_id: int, db: Session = Depends(get_db)):
    db_item = fetch_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
