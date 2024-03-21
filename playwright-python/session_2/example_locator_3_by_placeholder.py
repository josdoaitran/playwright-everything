import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    await page.goto("https://www.saucedemo.com/")
    ## Example get locator of element by placeholder
    username_texbox = page.get_by_placeholder("Username")
    await username_texbox.highlight()
    await username_texbox.fill("testing4everyone")
    password_textbox = page.get_by_placeholder("Password")
    await password_textbox.highlight()
    await password_textbox.fill("password of testing4everyone")
    await browser.close()

    # # Example get locator of element - but issues
    # await page.goto("https://bootswatch.com/default/")
    # username_texbox = page.get_by_placeholder("Password")
    # await username_texbox.highlight()
    # await username_texbox.fill("aaaaaa")
    # await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())