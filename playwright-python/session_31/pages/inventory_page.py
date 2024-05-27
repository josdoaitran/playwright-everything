from playwright.sync_api import ElementHandle
from playwright.sync_api import Page, expect
from session_31.pages.base_page import Base
class InventoryPage(Base):

    @property
    def app_logo(self) -> ElementHandle:
        return self.page.locator("//div[@class='app_logo']")


    def verify_inventory_page(self, page: Page):
        expect(self.app_logo).to_be_visible()