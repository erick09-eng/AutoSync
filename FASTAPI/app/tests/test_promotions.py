#app/tests/test_promotions.py
"""Promotion API tests module.
This module contains tests for the promotion API endpoints.
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

# Test to create a new promotion 
def test_create_promotion(client):
    """Test to create a new promotion."""
    response = client.post("/api/v1/promotions/", json={
        "name": "Test Promotion",
        "description": "This is a test promotion",
        "discount_type": "percentage",
        "discount_value": 10.0,
        "start_date": "2023-08-01T12:00:00",
        "end_date": "2023-08-31T23:59:59",
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Promotion"
    assert data["description"] == "This is a test promotion"
    assert data["discount_type"] == "percentage"
    assert data["discount_value"] == 10.0
    assert data["start_date"] == "2023-08-01T12:00:00"
    assert data["end_date"] == "2023-08-31T23:59:59"
    assert data["is_active"] is True
    assert "created_at" in data
    assert "promotion_id" in data

# Test to get a promotion by ID
def test_get_promotion(client):
    """Test to get a promotion by ID."""
    create_response = client.post("/api/v1/promotions/", json={
        "name" : "Test Promotion",
        "description" : "This is a test promotion",
        "discount_type" : "percentage",
        "discount_value" : 10.0,
        "start_date" : "2023-08-01T12:00:00",
        "end_date" : "2023-08-01T23:59:59",
        "is_active" : True
    })
    created_promotion = create_response.json()
    response = client.get(f"/api/v1/promotions/{created_promotion['promotion_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Promotion"

# Test to get all promotions
def test_get_promotions(client):
    """Test to get all promotions."""
    client.post("/api/v1/promotions/", json={
        "name" : "Test Promotion",
        "description" : "This is a test promotion",
        "discount_type" : "percentage",
        "discount_value" : 10.0,
        "start_date" : "2023-08-01T12:00:00",
        "end_date" : "2023-08-01T23:59:59",
        "is_active" : True
    })
    response = client.get("/api/v1/promotions/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a promotion
def test_update_promotion(client):
    """Test to update a promotion."""
    create_response = client.post("/api/v1/promotions/", json={
        "name" : "Test Promotion",
        "description" : "This is a test promotion",
        "discount_type" : "percentage",
        "discount_value" : 10.0,
        "start_date" : "2023-08-01T12:00:00",
        "end_date" : "2023-08-01T23:59:59",
        "is_active" : True
    })
    created_promotion = create_response.json()
    response = client.put(
        f"/api/v1/promotions/{created_promotion['promotion_id']}",
        json={"name" : "Updated Promotion",
        "description" : "This is an updated promotion",
        "discount_type" : "fixed",
        "discount_value" : 5.0,
        "start_date" : "2023-08-02T12:00:00",
        "end_date" : "2023-08-02T23:59:59",
        "is_active" : False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Promotion"
    assert data["description"] == "This is an updated promotion"
    assert data["discount_type"] == "fixed"
    assert data["discount_value"] == 5.0
    assert data["start_date"] == "2023-08-02T12:00:00"
    assert data["end_date"] == "2023-08-02T23:59:59"
    assert data["is_active"] is False

# Test to delete a promotion 
def test_delete_promotion(client):
    """Test to delete a promotion."""
    create_response = client.post("/api/v1/promotions/", json={
        "name" : "Test Promotion",
        "description" : "This is a test promotion",
        "discount_type" : "percentage",
        "discount_value" : 10.0,
        "start_date" : "2023-08-01T12:00:00",
        "end_date" : "2023-08-01T23:59:59",
        "is_active" : True
    })
    created_promotion = create_response.json()
    response = client.delete(f"/api/v1/promotions/{created_promotion['promotion_id']}")
    assert response.status_code == 200
    get_response = client.get(f"/api/v1/promotions/{created_promotion['promotion_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Promotion not found"
    