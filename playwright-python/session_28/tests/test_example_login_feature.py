from playwright.sync_api import Page
from session_28.pages.login_page import LoginPage
from session_28.pages.inventory_page import InventoryPage
import allure

@allure.feature("Login Feature")
@allure.story("Login Successfully")
@allure.title("Login with standard_user")
def test_login_tc_01(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.login("standard_user", "secret_sauce")
    inventory_page.verify_inventory_page(page)

@allure.feature("Login Feature")
@allure.story("Login Successfully")
@allure.title("Login with Performance_glitch_user")
def test_login_tc_02(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.login("performance_glitch_user", "secret_sauce")
    inventory_page.verify_inventory_page(page)
