import pytest
from feishu.web_test.page.app import App


@pytest.fixture(scope="session")
def app():
    app = App().start()
    yield app
    app.stop()
