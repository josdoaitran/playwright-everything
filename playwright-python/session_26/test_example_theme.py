from playwright.sync_api import Page
import pytest

# https://playwright.dev/python/docs/emulation

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        # "color_scheme": "light"
        "color_scheme": "dark"
    }
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

def test_example(page: Page):
    page.goto("https://playwright.dev/python/docs/emulation")
    page.pause()