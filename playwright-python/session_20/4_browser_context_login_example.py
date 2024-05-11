import logging
import pytest
from playwright.sync_api import Page

logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# Run test cases ordered / selected by browser types
# @pytest.mark.skip_browser("firefox")
# @pytest.mark.only_browser("firefox")
# -s -v  --headed --html=./report-results/report.html --capture=tee-sys --browser=firefox

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 5000
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": "./auth/storage_stage.json"
    }

@pytest.mark.skip_browser("firefox")
def test_website_login_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/inventory.html")
    logger.info(msg="Already Login successfully ")
    assert page.locator("//div[@class='app_logo']").is_visible()
    page.locator("//div[text()='Sauce Labs Backpack']/../../..//button").click()


@pytest.mark.only_browser("firefox")
def test_website_login_performance_glitch_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/inventory.html")
    logger.info(msg="Already Login successfully ")
    assert page.locator("//div[@class='app_logo']").is_visible()
    page.locator("//div[@class='header_label']/div").click()