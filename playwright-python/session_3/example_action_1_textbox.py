import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/text-box")
    # Example Click
    fullname_texbox = page.locator("//*[@id='userName']")
    await fullname_texbox.fill("Testing4Everyone")

    email_textbox = page.locator("//input[@id='userEmail']")
    await email_textbox.fill("testing4everyone@gmail.com")

    address_textarea = page.locator("//textarea[@id='currentAddress']")
    await address_textarea.fill("123 ABC, Block Z, Amazon Building, A City")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())