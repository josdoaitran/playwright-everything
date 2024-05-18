import pytest
from playwright.sync_api import Page
from session_27.pages.login_page import LoginPage
from session_27.pages.inventory_page import InventoryPage

# def test_example_tc(feature):
#     assert feature == "FEATURE"

def test_login_tc_01(page: Page):
    login_page = LoginPage(page)
    iventory_page = InventoryPage(page)
    login_page.login("standard_user", "secret_sauce")
    iventory_page.verify_inventory_page(page)

def test_login_tc_02(page: Page):
    login_page = LoginPage(page)
    iventory_page = InventoryPage(page)
    login_page.login("performance_glitch_user", "secret_sauce")
    iventory_page.verify_inventory_page(page)
