#app/services/inventory_movements_service.py
"""
This module defines the service layer for handling inventory movements in the system.
It includes functions for creating and retrieving inventory movements.
"""
from schemas.product_promotions import(
    ProductPromotionsCreate,
    ProductPromotionsResponse
)
from services.product_promotions_service import (create_product_promotion,
                                                 get_product_promotion,
                                                 get_all_product_promotions,
                                                 delete_product_promotion)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

# Create a new product promotion
@router.post("/", response_model=ProductPromotionsResponse)
def create_product_promotion_route(
    product_promotion: ProductPromotionsCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new product promotion.
    """
    return create_product_promotion(db, product_promotion)

# Get a product promotion by ID
@router.get("/{product_id}/{promotion_id}", response_model=ProductPromotionsResponse)
def read(
    product_id: int,
    promotion_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a product promotion by product ID and promotion ID.
    """
    product_promotion = get_product_promotion(db, product_id=product_id, promotion_id=promotion_id)
    if not product_promotion:
        raise HTTPException(status_code=404, detail="Product promotion not found")
    return product_promotion

# Get all product promotions
@router.get("/", response_model=list[ProductPromotionsResponse])
def get_all_product_promotions_route(
    db: Session = Depends(get_db)
):
    """
    Get all product promotions.
    """
    return get_all_product_promotions(db)

# Delete a product promotion
@router.delete("/{product_id}/{promotion_id}", response_model=dict)
def delete_product_promotion_route(
    product_id: int,
    promotion_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a product promotion.
    """
    deleted = delete_product_promotion(db, product_id=product_id, promotion_id=promotion_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product promotion not found")
    return {"detail": "Product promotion deleted successfully"}
