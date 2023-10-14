import helium as h
import pytest


@pytest.fixture(scope="class")
def _chrome_driver_init(request):
    request.cls.driver = h.start_chrome(headless=True)
    yield
    h.kill_browser()


class Basic_Chrome_Test:
    @pytest.fixture(scope="class", autouse=True)
    def _landing_page(self, _chrome_driver_init):
        h.go_to("http://localhost:8080/")
