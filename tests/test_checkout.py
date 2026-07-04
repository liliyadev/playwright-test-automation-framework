from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

from config.settings import (
    STANDARD_USERNAME,
    PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
)


def test_complete_checkout(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    overview = OverviewPage(page)
    complete = CompletePage(page)

    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart.click_checkout()

    checkout.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    overview.click_finish()

    assert complete.is_order_complete()