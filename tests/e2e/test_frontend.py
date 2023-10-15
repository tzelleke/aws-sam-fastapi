import helium as h

from .conftest import Basic_Chrome_Test


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_home_view(self):
        h.wait_until(
            h.Text("You did it!").exists,
            timeout_secs=1,
        )

        logo = h.Image("Vue logo")
        assert logo.exists()
        assert logo.width, logo.height == (125, 125)

    def test_nobel_prizes_view(self):
        h.click("Nobel Prizes")
        h.wait_until(
            h.Text("AWARD YEAR").exists,
            timeout_secs=1,
        )

    def test_nobel_laureates_view(self):
        h.click("Nobel Laureates")
        h.wait_until(
            h.Text("BIRTH DATE").exists,
            timeout_secs=1,
        )

    def test_api_docs(self):
        h.click("API Docs")
        h.wait_until(
            h.Text("Nobel Prize API").exists,
            timeout_secs=1,
        )
