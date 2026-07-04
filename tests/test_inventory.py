from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import STANDARD_USERNAME, PASSWORD


def test_add_backpack_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"


def test_remove_backpack_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.remove_backpack_from_cart()

    assert inventory.is_cart_empty()