#app/tests/test_inventory_movements.py
"""Inventory Movements API tests module.
This module contains tests for the inventory movements API endpoints.
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

# Test to create a new inventory movement
def test_create_inventory_movement(client):
    """
    Test to create a new inventory movement
    """
    response = client.post("/api/v1/inventory_movements/", json={
        "product_id": 1,
        "user_id": 1,
        "movement_type": "In",
        "quantity": 1,
        "reference_id": 1,
        "notes": "Test",
        "created_at": "2023-08-01T12:00:00"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == 1
    assert data["user_id"] == 1
    assert data["movement_type"] == "In"
    assert data["quantity"] == 1
    assert data["reference_id"] == 1
    assert data["notes"] == "Test"
    assert data["created_at"] == "2023-08-01T12:00:00"
    assert "movement_id" in data

# Test to get a inventory movement by ID
def test_get_inventory_movement(client):
    """
    Test to get a inventory movement by ID
    """
    create_response = client.post("/api/v1/inventory_movements/", json={
        "product_id": 1,
        "user_id": 1,
        "movement_type": "In",
        "quantity": 1,
        "reference_id": 1,
        "notes": "Test",
        "created_at": "2023-08-01T12:00:00"
    })
    created_movement = create_response.json()
    response = client.get(f"/api/v1/inventory_movements/{created_movement['movement_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == 1
    assert data["user_id"] == 1
    assert data["movement_type"] == "In"

# Test to get all inventory movements
def test_get_all_inventory_movements(client):
    """
    Test to get all inventory movements
    """
    client.post("/api/v1/inventory_movements/", json={
        "product_id": 1,
        "user_id": 1,
        "movement_type": "In",
        "quantity": 1,
        "reference_id": 1,
        "notes": "Test",
        "created_at": "2023-08-01T12:00:00"
    })
    response = client.get("/api/v1/inventory_movements/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a inventory movement
def test_update_inventory_movement(client):
    """
    Test to update a inventory movement
    """
    create_response = client.post("/api/v1/inventory_movements/", json={
        "product_id": 1,
        "user_id": 1,
        "movement_type": "In",
        "quantity": 1,
        "reference_id": 1,
        "notes": "Test",
        "created_at": "2023-08-01T12:00:00"
    })
    created_movement = create_response.json()

    # Update the movement 
    update_response = client.put(f"/api/v1/inventory_movements/{created_movement['movement_id']}", json={
        "product_id": 1,
        "user_id": 1,
        "movement_type": "Out",
        "quantity": 1,
        "reference_id": 1,
        "notes": "Updated Test",
        "created_at": "2023-08-01T12:00:00"
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["product_id"] == 1
    assert data["user_id"] == 1
    assert data["movement_type"] == "Out"
    assert data["quantity"] == 1
    assert data["reference_id"] == 1
    assert data["notes"] == "Updated Test"
    assert data["created_at"] == "2023-08-01T12:00:00"
    