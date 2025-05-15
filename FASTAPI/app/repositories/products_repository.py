#app/repositories/products_repository.py
"""
Products Repository
This module contains the functions to interact with the products table in the database.
It includes functions to create, read, update, and delete products.
"""
from models.product import Product
from schemas.product_schema import ProductCreate as ProductsCreate
from sqlalchemy.orm import Session

def create_product(db: Session, product: ProductsCreate):
    """Create a new product in the database.
    Args:
        db (Session): The database session.
        product (ProductsCreate): The product to create.
    Returns:
        ProductResponse: The created product.
    """
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    """Get a product by its ID.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product to retrieve.
    Returns:
        ProductResponse: The product with the specified ID.
    """
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session):
    """Get all products.
    Args:
        db (Session): The database session.
    Returns:
        list[ProductResponse]: A list of all products.
    """
    return db.query(Product).all()

def update_product(db: Session, product_id: int, product: ProductsCreate):
    """Update a product by its ID.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product to update.
        product (ProductsCreate): The updated product data.
    Returns:
        ProductResponse: The updated product.
    """
    db_product = get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()

def delete_product(db: Session, product_id: int):
    """Delete a product by its ID.
    Args:
        db (Session): The database session.
        product_id (int): The ID of the product to delete.
    """
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
