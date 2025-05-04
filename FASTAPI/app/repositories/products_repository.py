from sqlalchemy.orm import Session

from models.Product import Product as Products
from schemas.ProductSchema import ProductCreate as ProductsCreate, ProductResponse
from datetime import datetime

def create_product(db: Session, product: ProductsCreate):
    db_product = Products(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id).first()

def get_all_products(db: Session):
    return db.query(Products).all()

def update_product(db: Session, product_id: int, product: ProductsCreate):
    db_product = get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()