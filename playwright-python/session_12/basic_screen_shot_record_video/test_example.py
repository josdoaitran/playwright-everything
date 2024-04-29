from playwright.sync_api import Page, sync_playwright
import pytest
import logging
import os
from pathlib import Path
from slugify import slugify

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)


def delete_storage_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        logger.info("File deleted successfully.")
    else:
        logger.info("The file does not exist.")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra

# @pytest.fixture(autouse=True)
# def set_up_page(page: Page):
#     logger.info(msg="Configure Our Project")
#     logger.info(msg="Open Browser")
#     page.goto("https://www.saucedemo.com/")
#     # return page
#     yield page
#     logger.info(msg="Close Browser")
#     page.close()

# @pytest.fixture(scope="function")
# def set_up_page(page):
#     logger.info(msg="Configure Our Project")
#     logger.info(msg="Open Browser")
#     page.goto("https://www.saucedemo.com/")
#     # return page
#     yield page
#     logger.info(msg="Close Browser")
#     page.close()

# https://playwright.dev/python/docs/screenshots
def test_website_login_standard_user(page) -> None:
    # page = set_up_page
    # delete_storage_file("./screenshot/website_login_standard_user.png")
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()
    # page.pause()
    # page.screenshot(path="./screenshot/website_login_standard_user.png")

def test_website_login_performance_glitch_user(page) -> None:
    # page = set_up_page
    # delete_storage_file("./screenshot/website_login_performance_glitch_use.png")
    page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    username = page.locator("//input[@id='user-name1']")
    username.wait_for(timeout=1500)
    username.fill("performance_glitch_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//a[@class='shopping_cart_link']").is_visible()
    # page.pause()
    # page.screenshot(path="./screenshot/website_login_performance_glitch_use.png", full_page=True)

