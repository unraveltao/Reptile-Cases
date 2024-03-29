from playwright.sync_api import sync_playwright #导入同步模块
#创建Playwright管理器对象
with sync_playwright() as p: #p = sync_playwright()
    #基于p创建一个浏览器对象（谷歌浏览器对象）
    bro = p.chromium.launch(headless=False)
    #创建一个浏览器页面
    page = bro.new_page()
    #在指定的页面中进行请求发送
    page.goto('https://www.hut.edu.cn')
    #自行设置等待时长，注意：不可使用time.sleep
    page.wait_for_timeout(1000)
    #获取访问页面标题
    title = page.title()
    #获取页面的页面源码数据
    content = page.content()
    print(title,content)
    page.close()
    bro.close()