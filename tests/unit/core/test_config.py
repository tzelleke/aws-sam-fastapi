import pytest
from pytest import MonkeyPatch  # noqa: PT013

from app.core.config import Settings


@pytest.fixture()
def _env_var_aws_local(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_SAM_LOCAL", "TRUE")


@pytest.fixture()
def settings() -> Settings:
    return Settings()


def test_root_path_default(settings) -> None:
    assert settings.root_path == "/Prod"


@pytest.mark.usefixtures("_env_var_aws_local")
def test_root_path_overridden_in_local_env(settings) -> None:
    assert settings.root_path == ""
