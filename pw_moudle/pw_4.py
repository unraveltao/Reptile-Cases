from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro = p.chromium.launch(headless=False)
    page = bro.new_page()
    page.goto('https://www.baidu.com')


    # ===== 方案 1 =====
    input_tap = page.locator('#kw').press_sequentially('Hello World', delay = 500 )

    # ===== 方案 2 =====
    # 定位到输入框，进行文本录入
    # tag = page.locator('#kw')
    #
    # #设置内容的输入的时间间隔，实现一个一个字符的录入（模拟人的行为动作）
    # tag.focus() #聚焦于当前标签
    # input_text = 'Hello, World!'
    # for char in input_text:
    #     page.keyboard.type(char, delay=500)

    # 定位搜索按钮，进行点击操作
    page.locator('#su').click()

    page.close()
    bro.close()