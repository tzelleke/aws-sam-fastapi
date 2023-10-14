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

    def test_about_view(self):
        h.click("About")
        h.wait_until(
            h.Text("This is an about page").exists,
            timeout_secs=1,
        )

    def test_api_docs(self):
        h.click("API Docs")
        h.wait_until(
            h.Text("FastAPI AWS SAM").exists,
            timeout_secs=1,
        )
