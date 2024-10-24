import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base,get_db
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield client
    Base.metadata.drop_all(bind=engine)

def test_create_user(test_client):
    response = test_client.post(
        "/users/",
        json={"username": "testuser", "email": "testuser@example.com", "full_name": "Test User", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"
    assert response.json()["full_name"] == "Test User"

def test_get_user(test_client):
    response = test_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"
    assert response.json()["full_name"] == "Test User"

def test_update_user(test_client):
    response = test_client.put(
        "/users/1",
        json={"username": "updateduser", "email": "updateduser@example.com", "full_name": "Updated User"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
    assert response.json()["email"] == "updateduser@example.com"
    assert response.json()["full_name"] == "Updated User"

def test_delete_user(test_client):
    response = test_client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
    assert response.json()["email"] == "updateduser@example.com"
    assert response.json()["full_name"] == "Updated User"

    response = test_client.get("/users/1")
    assert response.status_code == 404
