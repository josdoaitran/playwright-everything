from playwright.sync_api import Page, BrowserContext
import pytest
import logging

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# configure igonore ssl
# refer to: https://playwright.dev/python/docs/test-runners

@pytest.fixture(autouse=True)
def trace_test_script(context: BrowserContext):
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield
    context.tracing.stop(path="trace.zip")

def test_website_login_standard_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()

def test_website_login_performance_glitch_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("performance_glitch_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//a[@class='shopping_cart_link']").is_visible()

