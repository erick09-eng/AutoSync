import json
from re import sub
import pytest  # Framework de pruebas
from fastapi.testclient import TestClient  # Cliente para probar la API
from sqlalchemy import create_engine  # Para crear la conexión a la base de datos
from sqlalchemy.orm import sessionmaker  # Para manejar sesiones de base de datos
from sqlalchemy.pool import StaticPool  # Para configurar el pool de conexiones
from app.main import app  # Importamos nuestra aplicación FastAPI
from app.db.database import Base
from app.db.session import get_db # Importamos la base y función para obtener la DB

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

# Test to create a new sale detail
def test_create_sale_detail(client):
    response = client.post("/api/v1/sales_details/", json={
        "sale_id": 1,
        "product_id": 1,
        "quantity": 1,
        "unit_price": 10.0,
        "discount_percentage": 0.0,
        "subtotal": 10.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["sale_id"] == 1
    assert data["product_id"] == 1
    assert data["quantity"] == 1
    assert data["unit_price"] == 10.0
    assert data["discount_percentage"] == 0.0
    assert data["subtotal"] == 10.0
    assert "sale_detail_id" in data

# Test to get a sale detail by ID
def test_get_sale_detail(client):
    create_response = client.get("/api/v1/sales_details/", json={
        "sale_id": 1,
        "product_id": 1,
        "quantity": 1,
        "unit_price": 10.0,
        "discount_percentage": 0.0,
        "subtotal": 10.0
    })
    created_sale_detail = create_response.json()
    response = client.get(f"/api/v1/sales_details/{created_sale_detail['sale_detail_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["sale_id"] == 1
