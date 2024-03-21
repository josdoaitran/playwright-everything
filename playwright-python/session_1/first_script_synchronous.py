# Using synchronous
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new tab
    page =  browser.new_page()
    # Navigate to "https://playwright.dev/"
    page.goto("https://playwright.dev/")
    # Click on Docs textlink
    doc_link = page.get_by_role("link", name = "Docs")
    doc_link.click()
    # Get URL and verify
    print("Docs: ", page.url)
    page.close()