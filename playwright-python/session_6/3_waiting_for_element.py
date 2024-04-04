# Using synchronous
from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    page.locator("//*[@id='2015']").click()
    print("=================================== START WAIT=======================================")
    start_time = perf_counter()
    # title = page.locator("//*[@id='table-body']/tr/td[1]").first.click()

    ########
    title = page.locator("//*[@id='table-body']/tr/td[1]").first
    title.wait_for(timeout=1500)
    title.click()
    time_taken = perf_counter() - start_time
    print(f"Page is loaded  in {round(time_taken, 2)}")