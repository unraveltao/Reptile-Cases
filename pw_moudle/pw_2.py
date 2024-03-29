import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        bro = await p.chromium.launch(headless=False,slow_mo=2000)
        page = await bro.new_page()
        await page.goto('https://www.baidu.com')
        title = await page.title()
        content = await page.content()
        print(title,content)
        await page.close()
        await bro.close()

asyncio.run(main())