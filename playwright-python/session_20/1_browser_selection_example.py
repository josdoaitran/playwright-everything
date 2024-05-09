import logging
import pytest
from playwright.sync_api import Page

logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# Run test cases ordered / selected by browser types
# @pytest.mark.skip_browser("firefox")
# @pytest.mark.only_browser("firefox")
# -s -v  --headed --html=./report-results/report.html --capture=tee-sys --browser=firefox
@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    yield page
    logger.info(msg="Close Browser")
    page.close()

@pytest.mark.skip_browser("firefox")
def test_website_login_standard_user(page: Page) -> None:
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()

@pytest.mark.only_browser("firefox")
def test_website_login_performance_glitch_user(page: Page) -> None:
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()
