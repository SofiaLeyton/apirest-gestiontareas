import pytest
import os

os.environ["DB_PATH"] = "test_tasks.db"

from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "description": "Testing"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test task"


def test_get_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200


def test_create_task_without_title(client):
    response = client.post(
        "/tasks",
        json={
            "description": "Missing title"
        }
    )

    assert response.status_code == 400