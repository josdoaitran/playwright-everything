# Using synchronous
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    # Simulate the case: can not find the element => timeout 30000ms exceeded. ~ 30 s
    doc_link = page.locator("//span[text()='Text Box']")
    # doc_link.click()
    # Change timeout waiting
    # doc_link.click(timeout=2_000)
    # Element is not visible, get locator but not visible to click
    doc_link.click(force= True)
    browser.close()