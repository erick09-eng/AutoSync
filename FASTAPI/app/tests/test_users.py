#app/tests/test_users.py
"""User API tests module.
This module contains tests for the user API endpoints.
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

# Test to create a new user
def test_create_user(client):
    """Create role"""
    role_response = client.post("/api/v1/roles/", json={
        "role_name": "Admin",
        "role_description": "Administrator role"
    })
    assert role_response.status_code == 200
    data_role = role_response.json()
    assert "role_id" in data_role

    """Test to create a new user."""
    response = client.post("/api/v1/users/", json={
        "username": "johndoe",
        "password_hash": "hashed_password123",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role_id": 1,
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "johndoe"
    assert data["password_hash"] == "hashed_password123"
    assert data["full_name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["role_id"] == 1
    assert data["is_active"] is True
    assert "created_at" in data
    assert "updated_at" in data
    assert "user_id" in data

# Test to get a user by its ID
def test_get_user_by_id(client):
    """Create role"""
    role_response = client.post("/api/v1/roles/", json={
        "role_name": "Admin",
        "role_description": "Administrator role"
    })
    assert role_response.status_code == 200
    data_role = role_response.json()
    assert "role_id" in data_role

    """Test to get a user by its ID."""
    create_response = client.post("/api/v1/users/", json={
        "username": "johndoe",
        "password_hash": "hashed_password123",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role_id": 1,
        "is_active": True
    })
    created_user = create_response.json()
    response = client.get(f"/api/v1/users/{created_user['user_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "johndoe"

# Test to get all users
def test_get_all_users(client):
    """Create role"""
    role_response = client.post("/api/v1/roles/", json={
        "role_name": "Admin",
        "role_description": "Administrator role"
    })
    assert role_response.status_code == 200
    data_role = role_response.json()
    assert "role_id" in data_role

    """Test to get all users."""
    client.post("/api/v1/users/", json={
        "username": "johndoe",
        "password_hash": "hashed_password123",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role_id": 1,
        "is_active": True
    })
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test to update an existing user
def test_update_user(client):
    """Create role"""
    role_response = client.post("/api/v1/roles/", json={
        "role_name": "Admin",
        "role_description": "Administrator role"
    })
    assert role_response.status_code == 200
    data_role = role_response.json()
    assert "role_id" in data_role

    """Test to update an existing user."""
    create_response = client.post("/api/v1/users/", json={
        "username": "johndoe",
        "password_hash": "hashed_password123",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role_id": 1,
        "is_active": True
    })
    created_user = create_response.json()

    #Update the user
    response = client.put(
        f"/api/v1/users/{created_user['user_id']}", 
        json={"username": "johndoe_updated",
        "password_hash": "hashed_password123_updated",
        "full_name": "John Doe Updated",
        "email": "john@updated.com",
        "role_id": 1,
        "is_active": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "johndoe_updated"
    assert data["password_hash"] == "hashed_password123_updated"
    assert data["full_name"] == "John Doe Updated"
    assert data["email"] == "john@updated.com"
    assert data["role_id"] == 1
    assert data["is_active"] is True

# Test to delete a user
def test_delete_user(client):
    """Create role"""
    role_response = client.post("/api/v1/roles/", json={
        "role_name": "Admin",
        "role_description": "Administrator role"
    })
    assert role_response.status_code == 200
    data_role = role_response.json()
    assert "role_id" in data_role

    """Test to delete a user."""
    create_response = client.post("/api/v1/users/", json={
        "username": "johndoe",
        "password_hash": "hashed_password123",
        "full_name": "John Doe",
        "email": "john@example.com",
        "role_id": 1,
        "is_active": True
    })
    created_user = create_response.json()
    response = client.delete(f"/api/v1/users/{created_user['user_id']}")
    assert response.status_code == 200
    get_response = client.get(f"/api/v1/users/{created_user['user_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "User not found"
    