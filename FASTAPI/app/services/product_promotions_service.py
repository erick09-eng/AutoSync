#services/product_promotions_service.py
from sqlalchemy.orm import Session
from app.models import ProductPromotions
from app.schemas import ProductPromotionsCreate, ProductPromotionsUpdate


def create_product_promotion(self, db: Session, product_promotion: ProductPromotionsCreate) -> ProductPromotions:
        """
        Create a new product promotion.
        """
        db_product_promotion = ProductPromotions(**product_promotion.dict())
        db.add(db_product_promotion)
        db.commit()
        db.refresh(db_product_promotion)
        return db_product_promotion
    
def get_product_promotion(self, db: Session, promotion_id: int) -> ProductPromotions:
        """
        Get a product promotion by ID.
        """
        return db.query(ProductPromotions).filter(ProductPromotions.id == promotion_id).first()
    
def get_all_product_promotions(self, db: Session) -> list[ProductPromotions]:
        """
        Get all product promotions.
        """
        return db.query(ProductPromotions).all()
def update_product_promotion(self, db: Session, promotion_id: int, product_promotion: ProductPromotionsUpdate) -> ProductPromotions:
        """
        Update a product promotion.
        """ 
        db_product_promotion = db.query(ProductPromotions).filter(ProductPromotions.id == promotion_id).first()
        if not db_product_promotion:
            return None
        for key, value in product_promotion.dict(exclude_unset=True).items():
            setattr(db_product_promotion, key, value)
        db.commit()
        db.refresh(db_product_promotion)
        return db_product_promotion
    
def delete_product_promotion(self, db: Session, promotion_id: int) -> bool:
        """
        Delete a product promotion.
        """
        db_product_promotion = db.query(ProductPromotions).filter(ProductPromotions.id == promotion_id).first()
        if not db_product_promotion:
            return False
        db.delete(db_product_promotion)
        db.commit()
        return True
# Example usage
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.schemas import ProductPromotionsCreate, ProductPromotionsUpdate
# from app.services.product_promotions_service import ProductPromotionsService