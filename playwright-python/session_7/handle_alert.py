from playwright.sync_api import sync_playwright, expect

def handle_accept_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.accept()
    print("Accept successfully")

def handle_cancel_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.dismiss()
    print("Cancel successfully")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # page.on("dialog", handle_accept_alert)
    # page.on("dialog", handle_cancel_alert)
    # page.on("dialog", lambda dialog: dialog.dismiss())
    page.on("dialog", lambda dialog: dialog.accept("Testing4Everyone"))

    page.goto("https://demoqa.com/alerts", wait_until='domcontentloaded')
    # page.locator("//button[@id='alertButton']").click()
    # page.locator("//button[@id='confirmButton']").click()
    page.locator("//button[@id='promtButton']").click()
    expect(page.locator("//span[@id='promptResult']")).to_contain_text("Testing4Everyone")

    page.close()
