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

#Test to create a new category
def test_create_category(client):
    response = client.post("/api/v1/categories/", json={
        "name": "Test Category", 
        "description": "Test Description", 
        "parent_category_id": None
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["description"] == "Test Description"
    assert data["parent_category_id"] == None
    assert "category_id" in data

# Test to get a category by its ID
def test_get_category(client):
    create_response = client.post("/api/v1/categories/", json={
        "name": "Test Category",
        "description": "Test Description",
        "parent_category_id": None
    })
    created_category = create_response.json()
    response = client.get(f"/api/v1/categories/{created_category['category_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"

# Test to get all categories
def test_get_all_categories(client):
    create_response = client.post("/api/v1/categories/", json={
        "name": "Test Category",
        "description": "Test Description",
        "parent_category_id": None
    })
    
    response = client.get("/api/v1/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

#Test to update an existing category
def test_update_category(client):
    create_response = client.post("/api/v1/categories/", json={
        "name": "Test Category",
        "description": "Test Description",
        "parent_category_id": None
    })
    created_category = create_response.json()
    
    update_response = client.put(
        f"/api/v1/categories/{created_category['category_id']}", 
        json={"name": "Updated Category",
        "description": "Updated Description",
        "parent_category_id": None
    })

    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Updated Category"
    assert data["description"] == "Updated Description"
    assert data["parent_category_id"] == None

#Test to delete a category
def test_delete_category(client):
    create_response = client.post("/api/v1/categories/", json={
        "name": "Test Category",
        "description": "Test Description",
        "parent_category_id": None
    })
    created_category = create_response.json()
    
    response = client.delete(f"/api/v1/categories/{created_category['category_id']}")
    assert response.status_code == 200

    get_response = client.get(f"/api/v1/categories/{created_category['category_id']}")
    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Category not found"
