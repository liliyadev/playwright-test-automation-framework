class OverviewPage:

    def __init__(self, page):
        self.page = page

    def click_finish(self):
        self.page.locator("#finish").click()