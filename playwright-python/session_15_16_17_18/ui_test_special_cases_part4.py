# UI Testing Spacial Case
from playwright.sync_api import Page, expect

# 10. Verify progress bar
# Example: http://www.uitestingplayground.com/progressbar
def test_verify_progress_bar(page: Page):
    page.goto("http://www.uitestingplayground.com/progressbar")
    start_btn = page.locator("button.btn-primary")
    stop_btn = page.locator("button.btn-info")
    progres_bar = page.locator("div.progress-bar")
    start_btn.click()
    while True:
        value = int(progres_bar.get_attribute("aria-valuenow"))
        if value >= 75:
            break
        else:
            print(f"Percentange: {value}%")
    stop_btn.click()
    expect(progres_bar).to_have_attribute("aria-valuenow", "75")
    assert value >= 75

