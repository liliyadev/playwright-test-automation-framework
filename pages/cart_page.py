class CartPage:

    def __init__(self, page):
        self.page = page

    def get_item_name(self):
        return self.page.locator(".inventory_item_name").inner_text()

    def is_backpack_in_cart(self):
        return self.get_item_name() == "Sauce Labs Backpack"

    def click_checkout(self):
        self.page.locator("#checkout").click()

    def continue_shopping(self):
        self.page.locator("#continue-shopping").click()