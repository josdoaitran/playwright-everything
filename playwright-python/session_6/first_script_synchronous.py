# Using synchronous
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page =  browser.new_page()
    page.goto("https://playwright.dev/")
    doc_link = page.get_by_role("link", name = "Docs")
    doc_link.click()
    page.close()