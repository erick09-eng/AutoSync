#api/v1/promotions_router.py
"""
promotions_router.py
This module defines the API endpoints for managing promotions in a FastAPI application.
It includes endpoints for creating, reading, updating, and deleting promotions.
Each endpoint uses the corresponding service function to interact with the database.
"""
from schemas.promotions import PromotionsCreate, PromotionsResponse
from services.promotions_service import (
    create_new_promotion,
    get_promotion_by_id,
    get_all_promotions_list,
    update_existing_promotion,
    delete_existing_promotion
)
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=PromotionsResponse)
def create_promotion(promotion: PromotionsCreate, db: Session = Depends(get_db)):
    """
    Create a new promotion.
    """
    return create_new_promotion(db, promotion)

@router.get("/{promotion_id}", response_model=PromotionsResponse)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    """
    Get a promotion by ID.
    """
    return get_promotion_by_id(db, promotion_id)

@router.get("/", response_model=list[PromotionsResponse])
def read_promotions(db: Session = Depends(get_db)):
    """
    Get all promotions.
    """
    return get_all_promotions_list(db)

@router.put("/{promotion_id}", response_model=PromotionsResponse)
def update_promotion(promotion_id: int, promotion: PromotionsCreate, db: Session = Depends(get_db)):
    """
    Update a promotion by ID.
    """
    return update_existing_promotion(db, promotion_id, promotion)

@router.delete("/{promotion_id}")
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    """
    Delete a promotion by ID.
    """
    return delete_existing_promotion(db, promotion_id)
