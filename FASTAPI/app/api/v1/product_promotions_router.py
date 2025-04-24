#api/v1/product_promotions_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
## from app.database import get_db
from app.schemas import ProductPromotionsCreate, ProductPromotionsUpdate, ProductPromotionsResponse
from app.services.product_promotions_service import ProductPromotionsService

router = APIRouter()
product_promotions_service = ProductPromotionsService()
# Create a new product promotion
@router.post("/", response_model=ProductPromotionsResponse)
def create_product_promotion(
    product_promotion: ProductPromotionsCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new product promotion.
    """
    return product_promotions_service.create_product_promotion(db, product_promotion)

# Get a product promotion by ID
@router.get("/{promotion_id}", response_model=ProductPromotionsResponse)
def get_product_promotion(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a product promotion by ID.
    """
    product_promotion = product_promotions_service.get_product_promotion(db, promotion_id)
    if not product_promotion:
        raise HTTPException(status_code=404, detail="Product promotion not found")
    return product_promotion

# Get all product promotions
@router.get("/", response_model=list[ProductPromotionsResponse])
def get_all_product_promotions(
    db: Session = Depends(get_db)
):
    """
    Get all product promotions.
    """
    return product_promotions_service.get_all_product_promotions(db)

# Update a product promotion
@router.put("/{promotion_id}", response_model=ProductPromotionsResponse)
def update_product_promotion(
    promotion_id: int,
    product_promotion: ProductPromotionsUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a product promotion.
    """
    updated_product_promotion = product_promotions_service.update_product_promotion(db, promotion_id, product_promotion)
    if not updated_product_promotion:
        raise HTTPException(status_code=404, detail="Product promotion not found")
    return updated_product_promotion

# Delete a product promotion
@router.delete("/{promotion_id}", response_model=dict)
def delete_product_promotion(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a product promotion.
    """
    deleted = product_promotions_service.delete_product_promotion(db, promotion_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product promotion not found")
    return {"detail": "Product promotion deleted successfully"}

