# main.py
from fastapi import FastAPI
from app.api.v1 import payments_router
from app.api.v1 import payment_methods_router
from app.api.v1 import sale_details_router
from app.api.v1 import inventory_movements_router
from app.api.v1 import promotions_router
from app.api.v1 import product_promotions_router



app = FastAPI()

app.include_router(sale_details_router.router, prefix="/api/v1/sales_details", tags=["sales_details"])
app.include_router(payments_router.router, prefix="/api/v1/payments", tags=["payments"])
app.include_router(payment_methods_router.router, prefix="/api/v1/promotions", tags=["promotions"])
app.include_router(inventory_movements_router.router, prefix="/api/v1/inventory_movements", tags=["inventory_movements"])
app.include_router(promotions_router.router, prefix="/api/v1/promotions", tags=["promotions"])
app.include_router(product_promotions_router.router, prefix="/api/v1/product_promotions", tags=["product_promotions"])