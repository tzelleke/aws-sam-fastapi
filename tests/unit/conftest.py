from fastapi.testclient import TestClient
import pytest


@pytest.fixture()
def client() -> TestClient:
    from app.main import app

    return TestClient(app)
