#app/api/v1/products_router.py
"""
    products_router.py
    This module defines the API routes for product management.
    It includes routes for creating, reading, updating, and deleting products.
    """
from services.product_service import (
    create_product,
    get_product,
    get_all_products,
    update_product,
    delete_product,
)
from schemas.product_schema import (
    ProductCreate as ProductsCreate,
    ProductResponse as ProductsResponse
    )
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=ProductsResponse)
def create(product: ProductsCreate, db: Session = Depends(get_db)):
    """Create a new product."""
    return create_product(db, product)

@router.get("/{product_id}", response_model=ProductsResponse)
def read(product_id: int, db: Session = Depends(get_db)):
    """Get a product by ID."""
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/", response_model=list[ProductsResponse])
def list_all(db: Session = Depends(get_db)):
    """Get all products."""
    return get_all_products(db)

@router.put("/{product_id}", response_model=ProductsResponse)
def update(product_id: int, product: ProductsCreate, db: Session = Depends(get_db)):
    """Update a product by ID."""
    updated_product = update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    """Delete a product by ID."""
    return delete_product(db, product_id)
