#app/repositories/products_repository.py
"""
Products Repository
This module contains the functions to interact with the products table in the database.
It includes functions to create, read, update, and delete products.
"""
from datetime import datetime, timezone, timedelta

from models.category import Category
from models.product import Product
from schemas.product_schema import(ProductCreate,
                                   ProductUpdate)
from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_colombia_time():
    """Get current time in Colombia timezone (UTC-5)."""
    colombia_tz = timezone(timedelta(hours=-5))
    return datetime.now(colombia_tz)

def create_product(db: Session, product: ProductCreate):
    """Create a new product in the database."""
    # validate the category_id exists in the database
    category = db.query(Category).filter(Category.category_id == product.category_id).first()
    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {product.category_id} not found"
        )

    # create dictionary for product data and add timestamps
    product_data = product.dict()
    product_data['created_at'] = get_colombia_time()
    product_data['updated_at'] = get_colombia_time()

    # create the product
    try:
        db_product = Product(**product_data)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while creating the product: {str(e)}"
        ) from e

def get_product(db: Session, product_id: int):
    """Get a product by its ID.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product to retrieve.
    Returns:
        ProductResponse: The product with the specified ID.
    """
    return db.query(Product).filter(Product.product_id == product_id).first()

def get_all_products(db: Session):
    """Get all products.
    Args:
        db (Session): The database session.
    Returns:
        list[ProductResponse]: A list of all products.
    """
    return db.query(Product).all()

def update_product(db: Session, product_id: int, product: ProductUpdate):
    """Update a product by its ID."""
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {product_id} not found"
        )

    data_product = product.dict(exclude_unset=True)
    data_product['updated_at'] = get_colombia_time()

    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """Delete a product by its ID.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product to delete.
    """
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {product_id} not found"
        )
    db.delete(db_product)
    db.commit()
    return {
        "message": f"Product with id {product_id} deleted successfully",
        "id": product_id
    }
