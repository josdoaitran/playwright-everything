from  playwright.sync_api import Page, Route
import pytest
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

def test_example_filter_all_iamge_css(page: Page):
    page.goto("https://katalon.com/")
    page.pause()
    page.screenshot(path="logs/image_no_disable_js.jpg", full_page=True)