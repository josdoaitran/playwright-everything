from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()
    page.close()