#app/services/product_promotions_service.py
"""
Service layer for managing product promotions.
This module contains functions to create, retrieve, update, and delete product promotions.
"""

from sqlalchemy.orm import Session
from models.product_promotions import ProductPromotions
from schemas.product_promotions import ProductPromotionsCreate


def create_product_promotion(
    db: Session,
    product_promotion:
        ProductPromotionsCreate
        ) -> ProductPromotions:
    """
    Create a new product promotion.
    Args:
        db (Session): Database session.
        product_promotion (ProductPromotionsCreate): Product promotion data.
        Returns:   """
    db_product_promotion = ProductPromotions(**product_promotion.dict())
    db.add(db_product_promotion)
    db.commit()
    db.refresh(db_product_promotion)
    return db_product_promotion

def get_product_promotion(db: Session, product_id: int, promotion_id: int) -> ProductPromotions:
    """Get a product promotion by product_id and promotion_id."""
    return db.query(ProductPromotions).filter(
        ProductPromotions.product_id == product_id,
        ProductPromotions.promotion_id == promotion_id
    ).first()

def get_all_product_promotions(db: Session) -> list[ProductPromotions]:
    """Get all product promotions."""
    return db.query(ProductPromotions).all()

def delete_product_promotion(db: Session, product_id: int, promotion_id: int) -> bool:
    """Delete a product promotion by product_id and promotion_id."""
    db_product_promotion = db.query(ProductPromotions).filter(
        ProductPromotions.product_id == product_id,
        ProductPromotions.promotion_id == promotion_id
    ).first()

    if db_product_promotion:
        db.delete(db_product_promotion)
        db.commit()
        return True
    return False

# Example usage
# from sqlalchemy.orm import Session
# from database import get_db
# from schemas import ProductPromotionsCreate, ProductPromotionsUpdate
# from services.product_promotions_service import ProductPromotionsService
