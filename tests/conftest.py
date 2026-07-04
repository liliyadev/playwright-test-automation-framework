import pytest


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()