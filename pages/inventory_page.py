class InventoryPage:

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.locator(".title").inner_text() == "Products"

    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def remove_backpack_from_cart(self):
        self.page.locator("#remove-sauce-labs-backpack").click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()

    def is_cart_empty(self):
        return self.page.locator(".shopping_cart_badge").count() == 0

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()