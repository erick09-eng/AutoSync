#app/tests/test_sales.py
"""Sale API tests module.
This module contains tests for the sale API endpoints.
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

# Test to create a new sale
def test_create_sale(client):
    """Test to create a new sale."""
    response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["document_type_id"] == 1
    assert data["serial_number"] == "1234567890"
    assert data["customer_id"] == 1
    assert data["user_id"] == 1
    assert data["subtotal"] == 12.0
    assert data["tax_amount"] == 1.0
    assert data["payment_method"] == 1
    assert "sale_id" in data

# Test to get a sale by its ID
def test_get_sale(client):
    """Test to get a sale by its ID."""
    create_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    created_sale = create_response.json()
    response = client.get(f"/api/v1/sales/{created_sale['sale_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["document_type_id"] == 1
    assert data["serial_number"] == "1234567890"

# Test to update a sale by ID
def test_update_sale(client):
    """Test to update a sale by ID."""
    create_response = client.post("/api/v1/sales/", json={
        "document_type_id": 1,
        "serial_number": "1234567890",
        "customer_id": 1,
        "user_id": 1,
        "subtotal": 12.0,
        "tax_amount": 1.0,
        "payment_method": 1
    })
    created_sale = create_response.json()
    
    # Update the sale
    update_response = client.put(
        f"/api/v1/sales/{created_sale['sale_id']}",
        json={"document_type_id": 2,
            "serial_number": "9876543210",
            "customer_id": 2,
            "user_id": 2,
            "subtotal": 11.0,
            "tax_amount": 0.5,
            "payment_method": 2
    })

    assert update_response.status_code == 200
    data = update_response.json()
    assert data["document_type_id"] == 2
    assert data["serial_number"] == "9876543210"
    assert data["customer_id"] == 2
    assert data["user_id"] == 2
    assert data["subtotal"] == 11.0
    assert data["tax_amount"] == 0.5
    assert data["payment_method"] == 2
    