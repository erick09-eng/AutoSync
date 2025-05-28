#app/services/product_promotions_service.py
"""
Service layer for managing product promotions.
This module contains functions to create, retrieve, update, and delete product promotions.
"""

from repositories import product_promotions_repository
from schemas.product_promotions import ProductPromotionsCreate, ProductPromotionsResponse
from sqlalchemy.orm import Session

def create_product_promotion(
    db: Session, product_promotion: ProductPromotionsCreate) -> ProductPromotionsResponse:
    """Create a new product promotion."""
    return product_promotions_repository.create_product_promotion(db, product_promotion)

def get_product_promotion(db: Session, product_id: int,
                          promotion_id: int) -> ProductPromotionsResponse:
    """Get a product promotion by product_id and promotion_id."""
    return product_promotions_repository.get_product_promotion_by_ids(
        db, product_id, promotion_id)

def get_all_product_promotions(db: Session) -> list[ProductPromotionsResponse]:
    """Get all product promotions."""
    return product_promotions_repository.get_all_product_promotions(db)

def delete_product_promotion(db: Session, product_id: int, promotion_id: int) -> bool:
    """Delete a product promotion by product_id and promotion_id."""
    return product_promotions_repository.delete_product_promotion(
        db, product_id, promotion_id)
