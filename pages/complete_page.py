class CompletePage:

    def __init__(self, page):
        self.page = page

    def is_order_complete(self):
        return self.page.locator(".complete-header").inner_text() == "Thank you for your order!"