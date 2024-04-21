from playwright.sync_api import Page, sync_playwright
import pytest


@pytest.fixture()
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    return browser.new_page()


def test_website(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
