# UI Testing Spacial Case
from playwright.sync_api import Page, expect
import pytest

# 10. Verify progress bar
# Example: http://www.uitestingplayground.com/progressbar
# Create a test that clicks Start button and then waits for the progress bar to reach 35%.
# Then the test should click Stop.
# The less the differnce between value of the stopped progress bar and 35% the better your result.
def test_verify_progress_bar(page: Page):
    page.goto("http://www.uitestingplayground.com/progressbar")
    start_btn = page.locator("button.btn-primary")
    stop_btn = page.locator("button.btn-info")
    progres_bar = page.locator("div.progress-bar")
    start_btn.click()
    while True:
        value = int(progres_bar.get_attribute("aria-valuenow"))
        if value >= 35:
            break
        else:
            print(f"Percentange: {value}%")
    stop_btn.click()
    expect(progres_bar).to_have_attribute("aria-valuenow", "35")
    assert value >= 35

# 11. Test visibility
# Example: http://www.uitestingplayground.com/visibility
def test_visibility(page: Page):
    page.goto("http://www.uitestingplayground.com/visibility")

    hidden_btn = page.locator("//button[@id='hideButton']")
    removed_btn = page.locator("//button[@id='removedButton']")
    zero_width_btn = page.locator("//button[@id='zeroWidthButton']")
    over_lapped_btn = page.locator("//button[@id='overlappedButton']")
    opacity_btn = page.locator("//button[@id='transparentButton']")
    visibility_hiden_btn = page.locator("//button[@id='invisibleButton']")
    display_none_btn = page.locator("//button[@id='notdisplayedButton']")
    offscreen_btn = page.locator("//button[@id='offscreenButton']")

    expect(hidden_btn).to_be_visible()
    expect(removed_btn).to_be_visible()
    expect(zero_width_btn).to_be_visible()
    expect(over_lapped_btn).to_be_visible()
    expect(opacity_btn).to_be_visible()
    expect(visibility_hiden_btn).to_be_visible()
    expect(display_none_btn).to_be_visible()
    expect(offscreen_btn).to_be_visible()

    hidden_btn.click()
    # Case: Hidden button is hidden => remove from HTML
    expect(removed_btn).to_be_hidden()
    # Case: zero_width_btn => verify attribute css width = 0
    expect(zero_width_btn).to_have_css("width", "0px")
    # Case: over_lapped_btn => verify a new div is created
    expect(page.locator("//div[@id='hidingLayer']")).to_be_visible()
    with pytest.raises(Exception):
        expect(over_lapped_btn).to_be_visible(timeout=1000)
        over_lapped_btn.click(timeout=1000)