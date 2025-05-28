#app/repositories/promotions_repository.py
"""Promotions Repository
This module contains the functions to interact with the promotions table in the database.
It includes functions to create, read, update, and delete promotions.
"""
from datetime import datetime,timezone, timedelta
from models.promotions import Promotions
from schemas.promotions import PromotionsCreate, PromotionsResponse
from sqlalchemy.orm import Session

def get_colombia_time():
    """Get current time in Colombia timezone (UTC-5)."""
    colombia_tz = timezone(timedelta(hours=-5))
    return datetime.now(colombia_tz)

def create_promotion(
    db: Session,
    promotion: PromotionsCreate
    ) -> PromotionsResponse:
    """Create a new promotion in the database.
    Args:
        db (Session): The database session.
        promotion (PromotionsCreate): The promotion to create.
    Returns:
        PromotionsResponse: The created promotion.
    """
    db_promotion = Promotions(
        name=promotion.name,
        description=promotion.description,
        discount_type=promotion.discount_type,
        discount_value=promotion.discount_value,
        start_date=promotion.start_date,
        end_date=promotion.end_date,
        is_active=promotion.is_active,
        created_at=get_colombia_time()
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def get_promotion(db: Session, promotion_id: int) -> PromotionsResponse:
    """Get a promotion by its ID.
    Args:
        db (Session): The database session.
        promotion_id (int): The ID of the promotion to retrieve.
        Returns:
            PromotionsResponse: The promotion with the specified ID.
    """
    return db.query(Promotions).filter(Promotions.promotion_id == promotion_id).first()

def get_all_promotions(db: Session) -> list[PromotionsResponse]:
    """Get all promotions.
    Args:
        db (Session): The database session.
    Returns:
        list[PromotionsResponse]: A list of all promotions.
    """
    return db.query(Promotions).all()

def update_promotion(
    db: Session,
    promotion_id: int,
    promotion: PromotionsCreate
    ) -> PromotionsResponse:
    """Update a promotion by its ID.
    Args:
        db (Session): The database session.
        promotion_id (int): The ID of the promotion to update.
        promotion (PromotionsCreate): The updated promotion data.
    Returns:
        PromotionsResponse: The updated promotion.
    """
    db_promotion = db.query(Promotions).filter(
        Promotions.promotion_id == promotion_id).first()
    if db_promotion:
        db_promotion.name = promotion.name
        db_promotion.description = promotion.description
        db_promotion.discount_type = promotion.discount_type
        db_promotion.discount_value = promotion.discount_value
        db_promotion.start_date = promotion.start_date
        db_promotion.end_date = promotion.end_date
        db_promotion.is_active = promotion.is_active
        db.commit()
        db.refresh(db_promotion)
    return db_promotion

def delete_promotion(db: Session, promotion_id: int) -> bool:
    """Delete a promotion by its ID.
    Args:
        db (Session): The database session.
        promotion_id (int): The ID of the promotion to delete.
    Returns:
        bool: True if the promotion was deleted, False otherwise.
    """
    db_promotion = db.query(Promotions).filter(
        Promotions.promotion_id == promotion_id).first()
    if db_promotion:
        db.delete(db_promotion)
        db.commit()
        return True
    return False
