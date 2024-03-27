import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/webtables")
    # Get and Verify all headers of Tables

    table_header = page.locator("//div[@role='columnheader']/div[@class='rt-resizable-header-content']")
    await expect(table_header).to_have_count(7)
    await expect(table_header.get_by_text("Salary")).to_be_visible()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())