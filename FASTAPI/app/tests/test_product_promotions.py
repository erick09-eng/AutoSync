#app/tests/test_product_promotions.py
"""Product Promotions API tests module.
This module contains tests for the product promotions API endpoints.
It uses pytest and fastapi.testclient to test the API.
"""
from venv import create
import pytest  # Framework de pruebas
from fastapi.testclient import TestClient  # Cliente para probar la API
from sqlalchemy import create_engine  # Para crear la conexión a la base de datos
from sqlalchemy.orm import sessionmaker  # Para manejar sesiones de base de datos
from sqlalchemy.pool import StaticPool  # Para configurar el pool de conexiones
from main import app  # Importamos nuestra aplicación FastAPI
from db.database import Base
from db.session import get_db  # Importamos la base y función para obtener la DB

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

# Test to create a new product promotion
def test_create_product_promotion(client):
    """Test to create a new product promotion."""
    response = client.post("/api/v1/product_promotions/", json={
        "product_id": 1,
        "promotion_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == 1
    assert data["promotion_id"] == 1

# Test to get a product promotion by ID
def test_get_product_promotion(client):
    """Test to get a product promotion by ID."""
    create_response = client.post("/api/v1/product_promotions/", json={
        "product_id": 1,
        "promotion_id": 1
    })
    created_product_promotion = create_response.json()
    response = client.get(f"/api/v1/product_promotions/{created_product_promotion['product_id']}/{created_product_promotion['promotion_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == created_product_promotion["product_id"]
    assert data["promotion_id"] == created_product_promotion["promotion_id"]

# Test to get all product promotions
def test_get_all_product_promotions(client):
    """Test to get all product promotions."""
    create_response = client.post("/api/v1/product_promotions/", json={
        "product_id": 1,
        "promotion_id": 1
    })
    response = client.get("/api/v1/product_promotions/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    
# Test to delete a product promotion
def test_delete_product_promotion(client):
    """Test to delete a product promotion."""
    create_response = client.post("/api/v1/product_promotions/", json={
        "product_id": 1,
        "promotion_id": 1
    })
    created_product_promotion = create_response.json()
    response = client.delete(f"/api/v1/product_promotions/{created_product_promotion['product_id']}/{created_product_promotion['promotion_id']}")
    assert response.status_code == 200
    get_response = client.get(f"/api/v1/product_promotions/{created_product_promotion['product_id']}/{created_product_promotion['promotion_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Product promotion not found"
    