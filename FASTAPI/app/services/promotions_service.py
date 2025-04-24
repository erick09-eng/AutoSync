#services/promotions_service.py
from sqlalchemy.orm import Session
from repositories.promotions_repository import (
    create_promotion,
    get_promotion,
    get_all_promotions,
    update_promotion,
    delete_promotion
)
from schemas.promotions import PromotionsCreate, PromotionsResponse
from fastapi import HTTPException, status
from datetime import datetime

def create_new_promotion(db: Session, promotion: PromotionsCreate) -> PromotionsResponse:
    """
    Create a new promotion in the database.
    """
    try:
        return create_promotion(db, promotion)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
def get_promotion_by_id(db: Session, promotion_id: int) -> PromotionsResponse:
    """
    Get a promotion by its ID.
    """
    promotion = get_promotion(db, promotion_id)
    if not promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    return promotion

def get_all_promotions_list(db: Session) -> list[PromotionsResponse]:
    """
    Get a list of all promotions.
    """
    try:
        return get_all_promotions(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
def update_existing_promotion(db: Session, promotion_id: int, promotion: PromotionsCreate) -> PromotionsResponse:
    """
    Update an existing promotion.
    """
    existing_promotion = get_promotion(db, promotion_id)
    if not existing_promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    
    try:
        return update_promotion(db, promotion_id, promotion)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
def delete_existing_promotion(db: Session, promotion_id: int) -> bool:
    """
    Delete a promotion by its ID.
    """
    existing_promotion = get_promotion(db, promotion_id)
    if not existing_promotion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    
    try:
        return delete_promotion(db, promotion_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
# This code is a service layer for handling promotions in a FastAPI application.
# It interacts with the repository layer to perform CRUD operations on promotions.
# The service layer is responsible for business logic and error handling.