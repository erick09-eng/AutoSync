#repositories/product_promotions_repository.py
from sqlalchemy.orm import Session
from app.models.product_promotions import ProductPromotions
from app.schemas.product_promotions import ProductPromotionsCreate

def create_product_promotion(db: Session, product_promotion: ProductPromotionsCreate):
    """
    Create a new product promotion.
    """
    db_product_promotion = ProductPromotions(**product_promotion.dict())
    db.add(db_product_promotion)
    db.commit()
    db.refresh(db_product_promotion)
    return db_product_promotion

def get_product_promotion_by_id(db: Session, product_promotion_id: int):
    """
    Get a product promotion by ID.
    """
    return db.query(ProductPromotions).filter(ProductPromotions.product_promotion_id == product_promotion_id).first()

def get_all_product_promotions(db: Session):
    """
    Get all product promotions.
    """
    return db.query(ProductPromotions).all()

def update_product_promotion(db: Session, product_promotion_id: int, product_promotion: ProductPromotionsCreate):
    """
    Update an existing product promotion by ID.
    """
    db_product_promotion = db.query(ProductPromotions).filter(ProductPromotions.product_promotion_id == product_promotion_id).first()
    if db_product_promotion:
        for key, value in product_promotion.dict().items():
            setattr(db_product_promotion, key, value)
        db.commit()
        db.refresh(db_product_promotion)
        return db_product_promotion
    return None

def delete_product_promotion(db: Session, product_promotion_id: int):
    """
    Delete a product promotion by ID.
    """
    db_product_promotion = db.query(ProductPromotions).filter(ProductPromotions.product_promotion_id == product_promotion_id).first()
    if db_product_promotion:
        db.delete(db_product_promotion)
        db.commit()
        return True
    return False

# This code defines the repository functions for managing product promotions in a FastAPI application.
# It includes functions for creating, reading, updating, and deleting product promotions.
# Each function interacts with the database using SQLAlchemy ORM.
# The code also includes error handling to return appropriate responses based on the operation's success or failure.