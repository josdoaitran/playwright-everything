import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://dev.to/")

    ## Example get locator of element by test_id
    test_id_example = page.get_by_test_id("main-nav")
    await test_id_example.highlight()
    print(await test_id_example.text_content())
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())