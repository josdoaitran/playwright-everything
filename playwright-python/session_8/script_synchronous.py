# Using synchronous
from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page =  browser.new_page()
    start_time = perf_counter()

    page.goto("https://playwright.dev/", wait_until="load")
    doc_link = page.get_by_role("link", name = "Docs")
    doc_link.click()
    time_taken = perf_counter() - start_time
    print(f"Page is loaded  in {round(time_taken, 2)}")
    page.close()