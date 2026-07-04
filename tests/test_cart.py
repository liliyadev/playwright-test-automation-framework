from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.settings import STANDARD_USERNAME, PASSWORD


def test_backpack_is_added_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.open_cart()

    assert cart.is_backpack_in_cart()