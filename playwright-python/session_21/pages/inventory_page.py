from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.app_logo = page.locator("//div[@class='app_logo']")


    def verify_inventory_page(self, page: Page):
        expect(self.app_logo).to_be_visible()
