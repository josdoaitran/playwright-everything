# Using synchronous
from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    ## wait_until = load => load all contents of page: image, ...
    # print ("=================================== START =======================================")
    # start_time = perf_counter()
    # # Load to page
    # page.goto("https://demoqa.com/automation-practice-form", wait_until='load')
    # # Loaded
    # time_taken = perf_counter() - start_time
    # print(f"Page is loaded  in {round(time_taken, 2)}")

    ## wait_until = domcontentloaded => load html, dom only ... no wait all static content
    # print("=================================== START =======================================")
    # start_time = perf_counter()
    # # Load to page
    # page.goto("https://demoqa.com/automation-practice-form", wait_until = 'domcontentloaded')
    # # Loaded
    # time_taken = perf_counter() - start_time
    # print(f"Page is loaded  in {round(time_taken, 2)}")

    ## wait_until = commit => Send request to server and instantly receive response to do next
    # print("=================================== START =======================================")
    # start_time = perf_counter()
    # # Load to page
    # page.goto("https://demoqa.com/automation-practice-form", wait_until='commit')
    # # Loaded
    # time_taken = perf_counter() - start_time
    # print(f"Page is loaded  in {round(time_taken, 2)}")

    # wait_until = networkidle => wait untile network in browser idle
    print("=================================== START =======================================")
    start_time = perf_counter()
    # Load to page
    page.goto("https://demoqa.com/automation-practice-form", wait_until='networkidle')
    # Loaded
    time_taken = perf_counter() - start_time
    print(f"Page is loaded  in {round(time_taken, 2)}")