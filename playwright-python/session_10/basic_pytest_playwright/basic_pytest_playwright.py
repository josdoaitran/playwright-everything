from playwright.sync_api import Page, sync_playwright
import pytest
import logging

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# configure igonore ssl
# refer to: https://playwright.dev/python/docs/test-runners#ignore-https-errors
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }

@pytest.fixture(scope="function", autouse=True)
def set_up_browser(page: Page):
    logger.info(msg="Configure Our Project")
    # playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    yield

def test_website_login_standard_user(page: Page):
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()
    page.close()

def test_website_login_performance_glitch_user(page: Page):
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("performance_glitch_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()
    page.close()
