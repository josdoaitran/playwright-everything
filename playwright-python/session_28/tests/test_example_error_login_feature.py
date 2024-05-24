from playwright.sync_api import Page
from session_28.pages.login_page import LoginPage
import allure

wrong_credential = "Epic sadface: Username and password do not match any user in this service"
lock_message = "Epic sadface: Sorry, this user has been locked out."

@allure.feature("Login Feature")
@allure.story("Login Unsuccessfully")
@allure.title("Login with wrong credential")
def test_login_failed_tc_01(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user1", "secret_sauce")
    login_page.verify_login_failed_alert_message()
    login_page.verify_login_failed_content_message(wrong_credential)

@allure.feature("Login Feature")
@allure.story("Login Unsuccessfully")
@allure.title("Login with locked_out_user")
def test_login_failed_tc_02(page: Page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.verify_login_failed_alert_message()
    login_page.verify_login_failed_content_message(lock_message)