import json
from pathlib import Path

from fastapi.testclient import TestClient
from httpx import Response
import pytest

data_dir = Path(__file__).parent.parent.parent / "data"
api_response_nobel_laureates = json.loads(
    (data_dir / "api_response_nobel_laureates.json").read_text()
)
response_nobel_laureates = json.loads(
    (data_dir / "response_nobel_laureates.json").read_text()
)


@pytest.mark.usefixtures("_mock_http_client")
@pytest.mark.parametrize(
    "mock_httpx_response", [Response(200, json=api_response_nobel_laureates)]
)
def test_read_many(client: TestClient):
    response = client.get("/api/v1/nobel-laureates", params={"limit": 1})
    assert response.status_code == 200
    assert response.json() == response_nobel_laureates
