from playwright.sync_api import Page, sync_playwright
import pytest
import logging
import os

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)


def delete_storage_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        logger.info("File deleted successfully.")
    else:
        logger.info("The file does not exist.")

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Configure Our Project")
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    # return page
    yield page
    logger.info(msg="Close Browser")
    page.close()

def test_website_login_standard_user(set_up_page: Page):
    delete_storage_file("./screenshoot/website_login_standard_user.png")
    logger.info(msg="Input Username")
    set_up_page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    set_up_page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    set_up_page.locator("//input[@id='login-button']").click()
    assert set_up_page.locator("//div[@class='app_logo']").is_visible()
    set_up_page.screenshot(path="./screenshoot/website_login_standard_user.png")

def test_website_login_performance_glitch_user(set_up_page: Page):
    delete_storage_file("./screenshoot/website_login_performance_glitch_use.png")
    logger.info(msg="Input Username")
    set_up_page.locator("//input[@id='user-name']").fill("performance_glitch_user")
    logger.info(msg="Input password")
    set_up_page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    set_up_page.locator("//input[@id='login-button']").click()
    assert set_up_page.locator("//a[@class='shopping_cart_link']").is_visible()
    set_up_page.screenshot(path="./screenshoot/website_login_performance_glitch_use.png", full_page=True)

