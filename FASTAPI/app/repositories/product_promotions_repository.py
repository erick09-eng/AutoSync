#repositories/product_promotions_repository.py
from sqlalchemy.orm import Session
from models import product_promotions as Product_Promotions
from schemas.product_promotions import ProductPromotionsCreate

def create_product_promotion(db: Session, product_promotion: ProductPromotionsCreate):
    """
    Create a new product promotion.
    """
    db_product_promotion = Product_Promotions(**product_promotion.dict())
    db.add(db_product_promotion)
    db.commit()
    db.refresh(db_product_promotion)
    return db_product_promotion

def get_product_promotion_by_ids(db: Session, product_id: int, promotion_id: int):
    """
    Get a product promotion by composite keys.
    """
    return db.query(Product_Promotions).filter(
        Product_Promotions.product_id == product_id,
        Product_Promotions.promotion_id == promotion_id
    ).first()


def get_all_product_promotions(db: Session):
    return db.query(Product_Promotions).all()


def update_product_promotion(db: Session, product_id: int, promotion_id: int, update_data: ProductPromotionsCreate):
    db_product_promotion = db.query(Product_Promotions).filter(
        Product_Promotions.product_id == product_id,
        Product_Promotions.promotion_id == promotion_id
    ).first()
    
    if db_product_promotion:
        for key, value in update_data.dict().items():
            setattr(db_product_promotion, key, value)
        db.commit()
        db.refresh(db_product_promotion)
        return db_product_promotion
    return None


def delete_product_promotion(db: Session, product_id: int, promotion_id: int):
    """
    Delete a product promotion by composite keys.
    """
    db_product_promotion = db.query(Product_Promotions).filter(
        Product_Promotions.product_id == product_id,
        Product_Promotions.promotion_id == promotion_id
    ).first()
    
    if db_product_promotion:
        db.delete(db_product_promotion)
        db.commit()
        return True
    return False


# This code defines the repository functions for managing product promotions in a FastAPI application.
# It includes functions for creating, reading, updating, and deleting product promotions.
# Each function interacts with the database using SQLAlchemy ORM.
# The code also includes error handling to return appropriate responses based on the operation's success or failure.