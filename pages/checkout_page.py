class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)
        self.page.locator("#continue").click()