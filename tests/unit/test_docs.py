from fastapi.testclient import TestClient


def test_docs(client: TestClient):
    response = client.get("/docs")
    assert response.status_code == 200
