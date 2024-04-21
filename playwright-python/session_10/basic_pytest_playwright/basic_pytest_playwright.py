from playwright.sync_api import Page, sync_playwright
import pytest
import logging

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

@pytest.fixture()
def page():
    logger.info(msg="Configure Our Project")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    return browser.new_page()


def test_website(page: Page):
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
    logger.info(msg="Connect login")
