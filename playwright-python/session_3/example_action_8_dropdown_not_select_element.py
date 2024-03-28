import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    # Case: Not a Select Element
    await page.goto("https://demoqa.com/automation-practice-form")
    await page.locator("//div[@id='state']").click()
    await page.locator("//div[@class=' css-11unzgr']/div").get_by_text("NCR").click()
    await page.locator("//div[@id='state']").click()
    await page.locator("//div[@class=' css-11unzgr']/div").get_by_text("Haryana").click()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())