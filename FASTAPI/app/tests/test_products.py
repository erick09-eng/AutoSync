#app/tests/test_products.py
"""Product API tests module.
This module contains tests for the product API endpoints.
It uses pytest and fastapi.testclient to test the API.
"""
import pytest  # Framework de pruebas
from fastapi.testclient import TestClient  # Cliente para probar la API
from sqlalchemy import create_engine  # Para crear la conexión a la base de datos
from sqlalchemy.orm import sessionmaker  # Para manejar sesiones de base de datos
from sqlalchemy.pool import StaticPool  # Para configurar el pool de conexiones
from main import app  # Importamos nuestra aplicación FastAPI
from db.database import Base
from db.session import get_db # Importamos la base y función para obtener la DB

# Configuración de la base de datos de prueba
SQLALCHEMY_DATABASE_URL = (
    "sqlite:///:memory:"  # Usamos SQLite en memoria para las pruebas
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },  # Permitimos acceso desde diferentes hilos
    poolclass=StaticPool,  # Usamos StaticPool para mejor manejo de conexiones en pruebas
)
# Creamos la fábrica de sesiones para la base de datos
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Fixture para crear y limpiar la base de datos en cada prueba
@pytest.fixture(scope="function")
def test_db():
    Base.metadata.create_all(bind=engine)  # Creamos todas las tablas
    try:
        db = TestingSessionLocal()  # Creamos una sesión de prueba
        yield db  # Proporcionamos la sesión a la prueba
    finally:
        db.close()  # Cerramos la sesión
        Base.metadata.drop_all(bind=engine)  # Limpiamos todas las tablas


# Fixture para crear el cliente de pruebas
@pytest.fixture
def client(test_db):
    def override_get_db():  # Función para sobreescribir la dependencia de base de datos
        try:
            yield test_db
        finally:
            test_db.close()

    # Sobreescribimos la dependencia con nuestra versión de prueba
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:  # Creamos el cliente de pruebas
        yield test_client
    app.dependency_overrides.clear()  # Limpiamos las sobreescrituras

# Test to create a new product
def test_create_product(client):
    """Test to create a new product."""
    response = client.post("/api/v1/products/", json={
        "sku": "SKU123",
        "name": "Test Product",
        "description": "This is a test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["sku"] == "SKU123"
    assert data["name"] == "Test Product"
    assert data["description"] == "This is a test product"
    assert data["category_id"] == 1
    assert data["unit_price"] == 10.99
    assert data["cost_price"] == 10.0
    assert data["current_stock"] == 10
    assert data["min_stock"] == 1
    assert data["on_offer"] == True
    assert data["offer_price"] == 1.99
    assert data["is_active"] == True
    assert "product_id" in data
    assert "created_at" in data
    assert "updated_at" in data

# Test to get a product
def test_get_product(client):
    """Test to get a product."""
    create_response = client.post("/api/v1/products/", json={
        "sku": "SKU123",
        "name": "Test Product",
        "description": "This is a test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    created_product = create_response.json()
    response = client.get(f"/api/v1/products/{created_product['product_id']}")
    assert response.status.code == 200
    data = response.json()
    assert data["sku"] == "SKU123"
    assert data["name"] == "Test Product"

# Test to get all products
def test_get_all_products(client):
    """Test to get all products."""
    client.post("/api/v1/products/", json={
        "sku": "SKU123",
        "name": "Test Product",
        "description": "This is a test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update an existing product
def test_update_product(client):
    """Test to update an existing product."""
    create_response = client.post("/api/v1/products/", json={
        "sku": "SKU123",
        "name": "Test Product",
        "description": "This is a test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    created_product = create_response.json()

    response = client.put(f"/api/v1/products/{created_product['product_id']}", json={
        "sku": "SKU123",
        "name": "Updated Product",
        "description": "This is an updated test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["sku"] == "SKU123"
    assert data["name"] == "Updated Product"
    assert data["description"] == "This is an updated test product"
    assert data["category_id"] == 1
    assert data["unit_price"] == 10.99
    assert data["cost_price"] == 10.0
    assert data["current_stock"] == 10
    assert data["min_stock"] == 1
    assert data["on_offer"] == True
    assert data["offer_price"] == 1.99
    assert data["is_active"] == True

# Test to delete a product
def test_delete_product(client):
    """Test to delete a product."""
    create_response = client.post("/api/v1/products/", json={
        "sku": "SKU123",
        "name": "Test Product",
        "description": "This is a test product",
        "category_id": 1,
        "unit_price": 10.99,
        "cost_price": 10.0,
        "current_stock": 10,
        "min_stock": 1,
        "on_offer": True,
        "offer_price": 1.99,
        "is_active": True
    })
    created_product = create_response.json()
    response = client.delete(f"/api/v1/products/{created_product['product_id']}")
    assert response.status_code == 200
    get_response = client.get(f"/api/v1/products/{created_product['product_id']}")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Product not found"}
    