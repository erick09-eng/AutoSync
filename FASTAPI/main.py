# main.py
from fastapi import FastAPI
from api.v1 import item_routes

app = FastAPI()

app.include_router(item_routes.router, prefix="/api/v1/item")
