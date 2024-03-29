import asyncio
from playwright.async_api import async_playwright # 导入同步模块

# 封装一个特殊函数
async def main():
# 创建Playwright管理器对象
    async with async_playwright() as p: #p = sync_playwright()
        # 基于p创建一个浏览器对象（谷歌浏览器对象）
        bro = await p.chromium.launch(headless=False)
        # 创建一个浏览器页面
        page = await bro.new_page()
        # 在指定的页面中进行请求发送
        await page.goto('https://www.hut.edu.cn')
        # 自行设置等待时长，注意：不可使用time.sleep
        await page.wait_for_timeout(1000)
        # 获取访问页面标题
        title = await page.title()
        # 获取页面的页面源码数据
        content = await page.content()
        print(title,content)
        await page.close()
        await bro.close()
asyncio.run(main())