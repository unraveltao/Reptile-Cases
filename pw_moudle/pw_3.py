from playwright.sync_api import sync_playwright


# css选择器定位：page.locator()--参数：标签/id/层级/class 选择器
# 交互操作：
# - 点击元素， click() 方法
# - 元素内输入文本， fill() 方法

with sync_playwright() as p:
    # headless 指不显示页面  ； slow_mo 指全局等待时间
    bro = p.chromium.launch(headless=False, slow_mo=2000)
    page = bro.new_page()
    page.goto('https://www.baidu.com')

    # id定位 --> " # "
    # 定位到输入框，进行文本录入
    page.locator('#kw').fill('Python教程') # id定位 --> " # "
    # 定位搜索按钮，进行点击操作
    page.locator('#su').click()
    # 后退操作
    page.go_back()

    # class定位 --> " . "
    # class = "bst bg" 具有空格表示2者选其一填入即可
    page.locator('.s_ipt').fill('爬虫')
    page.locator('#su').click()

    # 标签+属性定位
    page.locator('input#kw').fill('人工智能')
    page.locator('#su').click()

    # 层级定位
    page.locator('#form > span > input#kw').fill('数据分析')
    page.locator('#su').click()

    page.close()
    bro.close()