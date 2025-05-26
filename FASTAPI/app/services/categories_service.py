#app/services/categories_service.py
""" Service for managing categories.
This module contains the functions to interact with the categories table in the database.
It includes functions to create, read, update, and delete categories.
"""
from repositories import categories_repository
from schemas.category_schema import CategoryCreate
from sqlalchemy.orm import Session

def create_category(db: Session, category: CategoryCreate):
    """Create a new category in the database.
    Args:
        db (Session): The database session.
        category (CategoryCreate): The category to create.
    Returns:
        Category: The created category.
    """
    return categories_repository.create_category(db, category)

def get_category(db: Session, category_id: int):
    """Get a category by its ID.
    Args:
        db (Session): The database session.
        category_id (int): The ID of the category to retrieve.
    Returns:
        Category: The category with the specified ID.
    """
    return categories_repository.get_category(db, category_id)

def get_all_categories(db: Session):
    """"Get all categories.
    Args:
        db (Session): The database session.
        Returns:
            list[Category]: A list of all categories.
    """
    return categories_repository.get_all_categories(db)

def update_category(db: Session,
                    category_id: int,
                    category: CategoryCreate):
    """Update a category by its ID."""
    return categories_repository.update_category(db, category_id, category)

def delete_category(db: Session, category_id: int):
    """Delete a category by its ID."""
    return categories_repository.delete_category(db, category_id)
