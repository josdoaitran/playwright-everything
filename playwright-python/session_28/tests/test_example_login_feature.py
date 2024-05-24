from playwright.sync_api import Page
from session_28.pages.login_page import LoginPage
from session_28.pages.inventory_page import InventoryPage

def test_login_tc_01(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.login("standard_user", "secret_sauce")
    inventory_page.verify_inventory_page(page)

def test_login_tc_02(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.login("performance_glitch_user", "secret_sauce")
    inventory_page.verify_inventory_page(page)
