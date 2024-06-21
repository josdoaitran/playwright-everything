from playwright.sync_api import Page
import pytest
import random

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

def test_ecommerce(page: Page):
    page.goto("https://bstackdemo.com/")
    item_list = ['iPhone 12', 'Phone 12 Mini', 'iPhone 12 Pro Max', 'iPhone 12 Pro']
    # item_name = 'iPhone 12 Mini'
    item_name = random.choice(item_list)
    formatted_string = "//p[text()='%s']/../div[@class='shelf-item__buy-btn']" %(item_name)
    page.locator(formatted_string).click()
    page.pause()