#api/v1/promotions_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.promotions import PromotionsCreate, PromotionsResponse
from app.services.promotions_service import (
    create_new_promotion,
    get_promotion_by_id,
    get_all_promotions_list,
    update_existing_promotion,
    delete_existing_promotion
)
from app.models.promotions import Promotions

router = APIRouter()
@router.post("/", response_model=PromotionsResponse, status_code=status.HTTP_201_CREATED)
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

@router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    """
    Delete a promotion by ID.
    """
    delete_existing_promotion(db, promotion_id)
    return {"detail": "Promotion deleted successfully"}
# This code defines the API endpoints for managing promotions in a FastAPI application.
# It includes endpoints for creating, reading, updating, and deleting promotions.
# Each endpoint uses the corresponding service function to interact with the database.
# The code also includes error handling to return appropriate HTTP status codes and messages.