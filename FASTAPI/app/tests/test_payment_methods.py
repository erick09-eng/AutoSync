#app/tests/test_payment_methods.py
"""Payment Methods API tests module.
This module contains tests for the payment methods API endpoints.
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

# Test to create a new payment method 
def test_create_payment_method(client):
    """Test to create a new payment method."""
    response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["payment_method_name"] == "Test Payment Method"
    assert data["description"] == "This is a test payment method"
    assert data["requires_authorization"] == True
    assert "payment_method_id" in data

# Test to get a payment method by ID
def test_get_payment_method(client):  
    """Test to get a payment method by ID."""
    create_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    created_payment_method = create_response.json()
    response = client.get(f"/api/v1/payment_methods/{created_payment_method['payment_method_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["payment_method_name"] == "Test Payment Method"

# Test to get all payment methods
def test_get_all_payment_methods(client):
    """Test to get all payment methods."""
    client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method 1",
        "description": "This is a test payment method 1",
        "requires_authorization": True
    })
    response = client.get("/api/v1/payment_methods/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a payment method
def test_update_payment_method(client):
    """Test to update a payment method."""
    create_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    created_payment_method = create_response.json()
    
    # Update the payment method
    response = client.put(
        f"/api/v1/payment_methods/{created_payment_method['payment_method_id']}", 
        json={"payment_method_name": "Updated Test Payment Method",
        "description": "This is an updated test payment method",
        "requires_authorization": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["payment_method_name"] == "Updated Test Payment Method"
    assert data["description"] == "This is an updated test payment method"
    assert data["requires_authorization"] == False

# Test to delete a payment method
def test_delete_payment_method(client):
    """Test to delete a payment method."""
    create_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    created_payment_method = create_response.json()
    response = client.delete(f"/api/v1/payment_methods/{created_payment_method['payment_method_id']}")
    assert response.status_code == 200
    get_response = client.get(f"/api/v1/payment_methods/{created_payment_method['payment_method_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Payment method not found"
    