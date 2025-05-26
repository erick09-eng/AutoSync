#app/services/product_service.py
"""Product service module.
This module contains the service functions for products.
Functions:
    create_product: Create a new product.
    get_product: Get a product by its ID.
    get_all_products: Get all products.
    update_product: Update an existing product.
    delete_product: Delete a product.
"""
from repositories import products_repository
from schemas.product_schema import ProductCreate as ProductsCreate
from sqlalchemy.orm import Session

def create_product(db: Session, product: ProductsCreate):
    """Create a new product."""
    return products_repository.create_product(db, product)

def get_product(db: Session, product_id: int):
    """Get a product by its ID."""
    return products_repository.get_product(db, product_id)

def get_all_products(db: Session):
    """Get all products."""
    return products_repository.get_all_products(db)

def update_product(db: Session, product_id: int, product: ProductsCreate):
    """Update an existing product."""
    return products_repository.update_product(db, product_id, product)

def delete_product(db: Session, product_id: int):
    """Delete a product."""
    return products_repository.delete_product(db, product_id)
