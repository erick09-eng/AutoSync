#app/main.py
"""Main Application
This module initializes the FastAPI application and includes all the routers for the API endpoints.
It sets up the root path and includes routers for various resources such as roles, 
users, products, sales, etc.
"""

from api.v1 import payments_router
from api.v1 import payment_methods_router
from api.v1 import sale_details_router
from api.v1 import inventory_movements_router
from api.v1 import promotions_router
from api.v1 import product_promotions_router

from api.v1 import roles_router
from api.v1 import users_router
from api.v1 import customers_router
from api.v1 import categories_router
from api.v1 import products_router
from api.v1 import document_types_router
from api.v1 import sales_router

from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

app = FastAPI(
    root_path="/autosync"
)

@app.get("/")
def read_root():
    """Root endpoint that returns a simple greeting. 
    It is used to verify that the API is running."""
    return {"Hello": "World"}

app.include_router(roles_router.router, prefix="/api/v1/roles", tags=["roles"])
app.include_router(document_types_router.router,
                   prefix="/api/v1/document_types", tags=["document_types"])
app.include_router(users_router.router, prefix="/api/v1/users", tags=["users"])
app.include_router(customers_router.router, prefix="/api/v1/customers", tags=["customers"])

app.include_router(categories_router.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(products_router.router, prefix="/api/v1/products", tags=["products"])

app.include_router(payment_methods_router.router,
                   prefix="/api/v1/payment_methods", tags=["payment_methods"])
app.include_router(sales_router.router, prefix="/api/v1/sales", tags=["sales"])
app.include_router(sale_details_router.router,
                   prefix="/api/v1/sales_details", tags=["sales_details"])
app.include_router(payments_router.router, prefix="/api/v1/payments", tags=["payments"])

app.include_router(inventory_movements_router.router,
                   prefix="/api/v1/inventory_movements", tags=["inventory_movements"])
app.include_router(promotions_router.router, prefix="/api/v1/promotions", tags=["promotions"])
app.include_router(product_promotions_router.router,
                   prefix="/api/v1/product_promotions", tags=["product_promotions"])
