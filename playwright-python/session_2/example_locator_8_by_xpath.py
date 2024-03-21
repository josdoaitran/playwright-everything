import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    ## Example get locator of element by Xpath
    search_textbox_example = page.locator("xpath=//*[@id='navbarColor01']/form/input")
    await search_textbox_example.highlight()
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())