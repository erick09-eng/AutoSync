#app/repositories/product_promotions_repository.py
"""Product Promotions Repository
This module contains the functions to interact with the product promotions table in the database.
It includes functions to create, read, update, and delete product promotions.
Each function interacts with the database using SQLAlchemy ORM.
The code also includes error handling to return appropriate 
responses based on the operation's success or failure.
"""
from models.product_promotions import ProductPromotions
from schemas.product_promotions import ProductPromotionsCreate
from sqlalchemy.orm import Session

def create_product_promotion(db: Session, product_promotion: ProductPromotionsCreate):
    """
    Create a new product promotion.
    """
    db_product_promotion = ProductPromotions(**product_promotion.dict())
    db.add(db_product_promotion)
    db.commit()
    db.refresh(db_product_promotion)
    return db_product_promotion

def get_product_promotion_by_ids(db: Session, product_id: int, promotion_id: int):
    """
    Get a product promotion by composite keys.
    """
    return db.query(ProductPromotions).filter(
        ProductPromotions.product_id == product_id,
        ProductPromotions.promotion_id == promotion_id
    ).first()

def get_all_product_promotions(db: Session):
    """Get all product promotions.
    Args:
        db (Session): The database session.
    Returns:
        list[ProductPromotions]: A list of all product promotions.
    """
    return db.query(ProductPromotions).all()

def update_product_promotion(
    db: Session,
    product_id: int,
    promotion_id: int,
    update_data: ProductPromotionsCreate):
    """Update a product promotion by composite keys.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product.
        promotion_id (int): The ID of the promotion.
        update_data (ProductPromotionsCreate): The data to update.
    returns:
        ProductPromotions: The updated product promotion.
    """
    db_product_promotion = db.query(ProductPromotions).filter(
        ProductPromotions.product_id == product_id,
        ProductPromotions.promotion_id == promotion_id
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
    db_product_promotion = db.query(ProductPromotions).filter(
        ProductPromotions.product_id == product_id,
        ProductPromotions.promotion_id == promotion_id
    ).first()

    if db_product_promotion:
        db.delete(db_product_promotion)
        db.commit()
        return True
    return False
