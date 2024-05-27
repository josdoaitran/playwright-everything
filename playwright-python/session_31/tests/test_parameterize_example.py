from playwright.sync_api import Page
from session_31.pages.login_page import LoginPage
from session_31.pages.inventory_page import InventoryPage
import pytest

@pytest.mark.parametrize(
    ("account", "password"),
    (
        ('standard_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce')
    )
)


def test_login_sauce_demo(account, password, page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.login(account, password)
    inventory_page.verify_inventory_page(page)
