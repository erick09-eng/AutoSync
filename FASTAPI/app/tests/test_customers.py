#app/tests/test_customers.py
"""Customer API tests module.
This module contains tests for the customer API endpoints.
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

# Test to create a new customer
def test_create_customer(client):
    """
    Test to create a new customer
    """
    response = client.post("/api/v1/customers/", json={
        "tax_id": "123456789",
        "full_name": "John Doe",
        "email": "john.c.calhoun@examplepetstore.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["tax_id"] == "123456789"
    assert data["full_name"] == "John Doe"
    assert data["email"] == "john.c.calhoun@examplepetstore.com"
    assert data["phone"] == "1234567890"
    assert data["address"] == "123 Main St"
    assert data["is_active"] is True
    assert "created_at" in data
    assert "updated_at" in data
    assert "customer_id" in data

# Test to get a customer by ID
def test_get_customer(client):
    """
    Test to get a customer by ID
    """
    create_response = client.post("/api/v1/customers/", json={
        "tax_id": "123456789",
        "full_name": "John Doe",
        "email": "john.c.calhoun@examplepetstore.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "is_active": True
    })
    created_customer = create_response.json()
    response = client.get(f"/api/v1/customers/{created_customer['customer_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["tax_id"] == "123456789"
    assert data["full_name"] == "John Doe"

# Test to get all customers
def test_get_all_customers(client):
    """
    Test to get all customers
    """
    client.post("/api/v1/customers/", json={
        "tax_id": "123456789",
        "full_name": "John Doe",
        "email": "john.c.calhoun@examplepetstore.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "is_active": True,
    })
    response = client.get("/api/v1/customers/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a customer
def test_update_customer(client):
    """
    Test to update a customer
    """
    create_response = client.post("/api/v1/customers/", json={
        "tax_id": "123456789",
        "full_name": "John Doe",
        "email": "john.c.calhoun@examplepetstore.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "is_active": True
    })
    created_customer = create_response.json()

    # Update the customer
    update_response = client.put(f"/api/v1/customers/{created_customer['customer_id']}", json={
        "tax_id": "987654321",
        "full_name": "Jane Smith",
        "email": "jane.m.pierce@example-pet-store.com",
        "phone": "9876543210",
        "address": "456 Elm St",
        "is_active": True
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["tax_id"] == "987654321"
    assert data["full_name"] == "Jane Smith"
    assert data["email"] == "jane.m.pierce@example-pet-store.com"
    assert data["phone"] == "9876543210"
    assert data["address"] == "456 Elm St"
    assert data["is_active"] is True

# Test to delete a customer
def test_delete_customer(client):
    """
    Test to delete a customer
    """
    create_response = client.post("/api/v1/customers/", json={
        "tax_id": "123456789",
        "full_name": "John Doe",
        "email": "john.c.calhoun@examplepetstore.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "is_active": True
    })
    created_customer = create_response.json()

    response = client.delete(f"/api/v1/customers/{created_customer['customer_id']}")
    assert response.status_code == 200
    
    get_response = client.get(f"/api/v1/customers/{created_customer['customer_id']}")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Customer not found"}
      