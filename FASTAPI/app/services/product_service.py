from repositories.roles_repository import RolesRepository
from schemas.roles import RolesCreate, RolesResponse
from sqlalchemy.orm import Session

def create_product(db: Session, product: ProductsCreate):
    return products_repository.create_product(db, product)

def get_product(db: Session, product_id: int):
    return products_repository.get_product(db, product_id)

def get_all_products(db: Session):
    return products_repository.get_all_products(db)

def update_product(db: Session, product_id: int, product: ProductsCreate):
   return products_repository.update_product(db, product_id, product)

def delete_product(db: Session, product_id: int):
    return products_repository.delete_product(db, product_id)
    