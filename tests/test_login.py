from pages.login_page import LoginPage

from config.settings import (
    STANDARD_USERNAME,
    PASSWORD,
    INVALID_PASSWORD,
)


def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)

    assert page.locator(".title").inner_text() == "Products"


def test_invalid_login(page):
    login = LoginPage(page)

    login.open()
    login.login(STANDARD_USERNAME, INVALID_PASSWORD)

    error_message = login.get_error_message()

    assert "Username and password do not match" in error_message