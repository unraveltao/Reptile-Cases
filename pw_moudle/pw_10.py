from playwright.sync_api import sync_playwright
import pandas as pd
from lxml import etree

search = input("请输入你想搜索的内容：")
#封装页面切换的函数
def switch_to_page(context,title):
    for page in context.pages:
        if title == page.title():
            #浏览器停留在此page页面
            page.bring_to_front()
            return page

with sync_playwright() as p:
    # 创建一个浏览器对象
    bro = p.chromium.launch(headless=False, slow_mo=1000)
    # 创建上下文管理对象
    context = bro.new_context()
    # 基于上下文管理对象打开一个page页面
    page = context.new_page()
    # 发送请求
    page.goto('https://www.bilibili.com')

    # xpath定位
    page.locator('//*[@id="nav-searchform"]/div[1]/input').fill(f'{search}')
    page.locator('//*[@id="nav-searchform"]/div[2]').click()

    # ===== 进行页面标题收集 =====
    # pages = context.pages
    # for sub_page in pages:
    #     # 遍历每一个page，打印起page标题
    #     print(sub_page.title())


    # page页面的切换
    select_page = switch_to_page(context, f'{search}-哔哩哔哩_Bilibili')
    # 获取切换后的page页面数据
    page_text = select_page.content()
    # 数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[3]/div/div')
    # 1. 创建数据表格
    table = pd.DataFrame(columns=['title','author'])
    index = 0
    for div in div_list:
        title = div.xpath('.//h3[@class="bili-video-card__info--tit"]/@title')[0]
        author = div.xpath('.//span[@class="bili-video-card__info--author"]/text()')[0]
        # print(title,author)
        # 2. 数据表格插入数据
        table.loc[index] = [title,author]
        index += 1
    # 3.将数据表格转化成 Excel
    table.to_excel('bilbil_search.xlsx')


    page.close()
    context.close()
    bro.close()