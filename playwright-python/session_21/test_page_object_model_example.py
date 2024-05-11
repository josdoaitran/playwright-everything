from session_21.pages.login_page import LoginPage
from session_21.pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

def test_login_tc_01(page: Page):
    login_page = LoginPage(page)
    iventory_page = InventoryPage(page)
    login_page.login("standard_user", "secret_sauce")
    iventory_page.verify_inventory_page(page)

def test_login_tc_02(page: Page):
    login_page = LoginPage(page)
    iventory_page = InventoryPage(page)
    login_page.login("standard_user1", "secret_sauce")
    login_page.verify_login_failed_alert_message()

