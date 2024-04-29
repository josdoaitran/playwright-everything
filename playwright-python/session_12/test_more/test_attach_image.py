from playwright.sync_api import Page, sync_playwright
import pytest
import logging
import os
from pathlib import Path
from slugify import slugify

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# https://playwright.dev/python/docs/screenshots
def test_website_login_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    # page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//div[@class='app_logo']").is_visible()

def test_website_login_performance_glitch_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    # page.goto("https://www.saucedemo.com/")
    logger.info(msg="Input Username")
    username = page.locator("//input[@id='user-name1']")
    username.wait_for(timeout=1500)
    username.fill("performance_glitch_user")
    logger.info(msg="Input password")
    page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    page.locator("//input[@id='login-button']").click()
    assert page.locator("//a[@class='shopping_cart_link']").is_visible()

