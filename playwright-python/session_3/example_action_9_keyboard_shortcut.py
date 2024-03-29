import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    # Case: Not a Select Element
    await page.goto("https://demoqa.com/automation-practice-form")
    await page.locator("//input[@id='firstName']").fill("TestingEveryoneOne")
    await page.locator("//input[@id='firstName']").fill("")

    await page.locator("//input[@id='firstName']").fill("TestingEveryoneOne")
    await page.locator("//input[@id='firstName']").clear()

    await page.locator("//input[@id='firstName']").press("KeyT")
    await page.locator("//input[@id='firstName']").press("KeyE")
    await page.locator("//input[@id='firstName']").clear()

    await page.locator("//input[@id='firstName']").press("Shift+KeyT")
    await page.locator("//input[@id='firstName']").press("KeyE")
    await page.locator("//input[@id='firstName']").press("KeyS")
    await page.locator("//input[@id='firstName']").press("KeyT")

    await page.locator("//input[@id='firstName']").press("ArrowLeft")

    await page.locator("//input[@id='firstName']").clear()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())