from collections.abc import Callable

from httpx import (
    AsyncClient,
    MockTransport,
    Request,
    Response,
)
import pytest


@pytest.fixture()
def mock_httpx_response() -> Response:
    return Response(204)


@pytest.fixture()
def mock_httpx_transport_handler(mock_httpx_response) -> Callable[[Request], Response]:
    def handler(_request: Request) -> Response:
        return mock_httpx_response

    return handler


@pytest.fixture()
def _mock_http_client(mock_httpx_transport_handler) -> None:
    from app.http import get_http_client
    from app.main import app

    async def get_http_client_mock() -> AsyncClient:
        async with AsyncClient(
            base_url="http://testserver",
            headers={"Accept": "application/json"},
            transport=MockTransport(mock_httpx_transport_handler),
        ) as client:
            yield client

    app.dependency_overrides[get_http_client] = get_http_client_mock

    yield

    del app.dependency_overrides[get_http_client]
