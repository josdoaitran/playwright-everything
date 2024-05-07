# UI Testing Spacial Case
from playwright.sync_api import Page, expect

# 10. Verify progress bar
# Example: http://www.uitestingplayground.com/progressbar
def test_verify_progress_bar(page: Page):
    page.goto("http://www.uitestingplayground.com/progressbar")


