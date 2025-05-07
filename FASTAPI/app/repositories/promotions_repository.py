#repositories/promotions_repository.py
from sqlalchemy.orm import Session
from models import promotions as Promotions
from schemas.promotions import PromotionsCreate, PromotionsResponse
from datetime import datetime

def create_promotion(db: Session, promotion: PromotionsCreate) -> PromotionsResponse:
    db_promotion = Promotions(
        name=promotion.name,
        description=promotion.description,
        discount_type=promotion.discount_type,
        discount_value=promotion.discount_value,
        start_date=promotion.start_date,
        end_date=promotion.end_date,
        is_active=promotion.is_active,
        created_at=datetime.now()
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def get_promotion(db: Session, promotion_id: int) -> PromotionsResponse:
    return db.query(Promotions).filter(Promotions.promotion_id == promotion_id).first()

def get_all_promotions(db: Session) -> list[PromotionsResponse]:
    return db.query(Promotions).all()

def update_promotion(db: Session, promotion_id: int, promotion: PromotionsCreate) -> PromotionsResponse:
    db_promotion = db.query(Promotions).filter(Promotions.promotion_id == promotion_id).first()
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
    db_promotion = db.query(Promotions).filter(Promotions.promotion_id == promotion_id).first()
    if db_promotion:
        db.delete(db_promotion)
        db.commit()
        return True
    return False

    