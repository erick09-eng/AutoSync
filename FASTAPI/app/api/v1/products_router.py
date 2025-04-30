from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.products_service import (
    create_product,
    get_product,
    get_all_products,
    update_product,
    delete_product,
)
from schemas.products_schema import ProductsCreate, ProductsResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductsResponse)
def create(product: ProductsCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/{product_id}", response_model=ProductsResponse)
def read(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/", response_model=list[ProductsResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.put("/{product_id}", response_model=ProductsResponse)
def update(product_id: int, product: ProductsCreate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product)

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
