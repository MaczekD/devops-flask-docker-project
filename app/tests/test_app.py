import pytest
from app.src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_users_endpoint(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json

def test_app_exists():
    assert app is not None
