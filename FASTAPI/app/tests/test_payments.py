#app/tests/test_payments.py
"""Payment API tests module.
This module contains tests for the payment API endpoints.
It uses pytest and fastapi.testclient to test the API.
"""
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

# Test to create a new payment record
def test_create_payment(client):
    """
    Test to create a new payment record
    """
    # Create sale
    sale_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    assert sale_response.status_code == 200
    sale_data = sale_response.json()
    assert "sale_id" in sale_data

    # Create payment method
    payment_method_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    assert payment_method_response.status_code == 200
    payment_method_data = payment_method_response.json()
    assert "payment_method_id" in payment_method_data

    # Create payment
    response = client.post("/api/v1/payments/", json={
        "sale_id": 1,
        "payment_method_id": 1,
        "amount": 10.0,
        "transaction_code": "ABC123",
        "status": "success"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["sale_id"] == 1
    assert data["payment_method_id"] == 1
    assert data["amount"] == 10.0
    assert data["transaction_code"] == "ABC123"
    assert data["status"] == "success"
    assert "payment_date" in data
    assert "payment_id" in data

# Test to get a payment record by its ID
def test_get_payment(client):
    """
    Test to get a payment record by its ID
    """
    # Create sale
    sale_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    assert sale_response.status_code == 200
    sale_data = sale_response.json()
    assert "sale_id" in sale_data

    # Create payment method
    payment_method_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    assert payment_method_response.status_code == 200
    payment_method_data = payment_method_response.json()
    assert "payment_method_id" in payment_method_data

    create_response = client.post("/api/v1/payments/", json={
        "sale_id": 1,
        "payment_method_id": 1,
        "amount": 10.0,
        "transaction_code": "ABC123",
        "status": "success"
    })
    created_payment = create_response.json()
    response = client.get(f"/api/v1/payments/{created_payment['payment_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["sale_id"] == 1
    assert data["payment_method_id"] == 1
    assert data["amount"] == 10.0
    assert data["transaction_code"] == "ABC123"
    assert data["status"] == "success"

# Test to get all payment records
def test_get_payments(client):
    """
    Test to get all payment records
    """
    # Create sale
    sale_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    assert sale_response.status_code == 200
    sale_data = sale_response.json()
    assert "sale_id" in sale_data

    # Create payment method
    payment_method_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    assert payment_method_response.status_code == 200
    payment_method_data = payment_method_response.json()
    assert "payment_method_id" in payment_method_data

    client.post("/api/v1/payments/", json={
        "sale_id": 1,
        "payment_method_id": 1,
        "amount": 10.0,
        "transaction_code": "ABC123",
        "status": "success"
    })
    response = client.get("/api/v1/payments/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a payment record
def test_update_payment(client):
    """
    Test to update a payment record
    """
    # Create sale
    sale_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    assert sale_response.status_code == 200
    sale_data = sale_response.json()
    assert "sale_id" in sale_data

    # Create payment method
    payment_method_response = client.post("/api/v1/payment_methods/", json={
        "payment_method_name": "Test Payment Method",
        "description": "This is a test payment method",
        "requires_authorization": True
    })
    assert payment_method_response.status_code == 200
    payment_method_data = payment_method_response.json()
    assert "payment_method_id" in payment_method_data

    create_response = client.post("/api/v1/payments/", json={
        "sale_id": 1,
        "payment_method_id": 1,
        "amount": 10.0,
        "transaction_code": "ABC123",
        "status": "success"
    })
    created_payment = create_response.json()
    
    #Update the payment
    update_response = client.put(
        f"/api/v1/payments/{created_payment['payment_id']}", json={
        "sale_id": 1,
        "payment_method_id": 1,
        "amount": 10.0,
        "transaction_code": "UPDATE123",
        "status": "success"
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["sale_id"] == 1
    assert data["payment_method_id"] == 1
    assert data["amount"] == 10.0
    assert data["transaction_code"] == "UPDATE123"
    assert data["status"] == "success" 
    