#services/product_promotions_service.py
from sqlalchemy.orm import Session
from models.product_promotions import Product_Promotions
from schemas.product_promotions import ProductPromotionsCreate


def create_product_promotion(db: Session, product_promotion: ProductPromotionsCreate) -> Product_Promotions:
        """
        Create a new product promotion.
        """
        db_product_promotion = Product_Promotions(**product_promotion.dict())
        db.add(db_product_promotion)
        db.commit()
        db.refresh(db_product_promotion)
        return db_product_promotion
    
def get_product_promotion(self, db: Session, product_id: int, promotion_id: int) -> Product_Promotions:
    return db.query(Product_Promotions).filter(
        Product_Promotions.product_id == product_id,
        Product_Promotions.promotion_id == promotion_id
    ).first()

    
def get_all_product_promotions(self, db: Session) -> list[Product_Promotions]:
    return db.query(Product_Promotions).all()

def delete_product_promotion(self, db: Session, product_id: int, promotion_id: int) -> bool:
    db_product_promotion = db.query(Product_Promotions).filter(
        Product_Promotions.product_id == product_id,
        Product_Promotions.promotion_id == promotion_id
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