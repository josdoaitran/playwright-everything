from pytest_bdd import scenarios, scenario, given, when, then, parsers
from session_32.pages.login_page import LoginPage
from session_32.pages.inventory_page import InventoryPage
from playwright.sync_api import Page
import pytest

# @scenario('../features/test_feature.feature', "Run login with scenario outline")
# def test_login():
#     pass

scenarios('../features/test_feature.feature')

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@given("I access to login Sauce Labs site")
def i_access_to_login_sauce_demo(login_page):
    # login_page = LoginPage(page)
    login_page.goto_base_url()

@when("I input valid credential on Sauce Labs login page")
def i_input_username_and_password_on_sauce_labs_login_page(login_page):
    # login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

@when(parsers.parse("I input {username_value} and {password_value} on Sauce Labs login page"))
def i_input_username_value_and_password_value_on_sauce_labs_login_page(login_page, username_value, password_value):
    # login_page = LoginPage(page)
    login_page.login(username_value, password_value)

@then("I can login successfully")
def i_can_login_successfully(page):
    inventory_page = InventoryPage(page)
    inventory_page.verify_inventory_page(page)