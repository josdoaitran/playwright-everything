from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page is loading: " , page)

def on_request(request):
    print("Requests be sent: ", request)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # page.on("load", on_load)
    page.on("request", on_request)
    page.goto("https://demoqa.com/automation-practice-form")
    page.close()





