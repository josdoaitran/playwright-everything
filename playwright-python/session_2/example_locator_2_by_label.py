import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    ## Example get locator of element by Label
    email_textbox = page.get_by_label("Password")
    await email_textbox.highlight()
    await browser.close()



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())