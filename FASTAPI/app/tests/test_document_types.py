#app/tests/test_document_types.py
"""Document Type API tests module.
This module contains tests for the document type API endpoints.
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

# Test to create a new document type
def test_create_document_type(client):
    """
    Test to create a new document type
    """
    response = client.post("/api/v1/document_types", json={
        "code": "TestCode",
        "name": "TestName",
        "description": "TestDescription"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "TestCode"
    assert data["name"] == "TestName"
    assert data["description"] == "TestDescription"
    assert "document_type_id" in data

# Test to get a document type by ID
def test_get_document_type(client):
    """
    Test to get a document type by ID
    """
    create_response = client.post("/api/v1/document_types", json={
        "code": "TestCode",
        "name": "TestName",
        "description": "TestDescription"
    })
    created_document_type = create_response.json()
    response = client.get(f"/api/v1/document_types/{created_document_type['document_type_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == "TestCode"

# Test to get all document types
def test_get_all_document_types(client):
    """
    Test to get all document types
    """
    client.post("/api/v1/document_types", json={
        "code": "TestCode1",
        "name": "TestName1",
        "description": "TestDescription1"
    })
    response = client.get("/api/v1/document_types")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update a document type
def test_update_document_type(client):
    """
    Test to update a document type
    """
    create_response = client.post("/api/v1/document_types", json={
        "code": "TestCode",
        "name": "TestName",
        "description": "TestDescription"
    })
    created_document_type = create_response.json()

    # Update the document type
    update_response = client.put(
        f"/api/v1/document_types/{created_document_type['document_type_id']}", 
        json={"code": "UpdatedCode",
        "name": "UpdatedName",
        "description": "UpdatedDescription"
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["code"] == "UpdatedCode"
    assert data["name"] == "UpdatedName"
    assert data["description"] == "UpdatedDescription"

# Test to delete a document type
def test_delete_document_type(client):
    """
    Test to delete a document type
    """
    create_response = client.post("/api/v1/document_types", json={
        "code": "TestCode",
        "name": "TestName",
        "description": "TestDescription"
    })
    created_document_type = create_response.json()

    response = client.delete(f"/api/v1/document_types/{created_document_type['document_type_id']}")
    assert response.status_code == 200

    get_response = client.get(f"/api/v1/document_types/{created_document_type['document_type_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Document type not found"
    