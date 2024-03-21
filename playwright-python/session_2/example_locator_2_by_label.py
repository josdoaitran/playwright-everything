import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    ## Example get locator of element by Label
    email_label = page.get_by_label("Password")
    await email_label.highlight()
    await browser.close()

    ## Explain error with find locator by label
    ## can not find the exact element
    ## if having more than 1 element with same label attribute value


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())