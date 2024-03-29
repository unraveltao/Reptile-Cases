from playwright.sync_api import sync_playwright
import os
os.system('playwright codegen --save-storage=taobao.json https://www.taobao.com')

with sync_playwright() as p:
    bro = p.chromium.launch(headless=False, slow_mo=2000)
    # context : 携带 cooike 进行信息操作
    context = bro.new_context(storage_state='taobao.json')

    page = context.new_page()
    page.goto('https://www.taobao.com')

    page.locator('input#q').fill('暗夜精灵 显示器')
    # class属性值为btn-search tb-bg，在定位的时候选择空格左右两侧任意一个属性值即可
    page.locator('button.btn-search').click()

    # 根据文本定位
    page.get_by_text('发货地').click()
    page.wait_for_timeout(1000)

    # 定位到满足要求所有的标签(商品列表最外层的a标签)
    locator = page.locator('.Content--contentInner--QVTcU0M > div > a')
    # 获得所有标签
    all_tag = locator.all()

    # 查看定位到满足要求标签的数量
    count = locator.count()
    print(count)

    # 定位到第10个a标签,nth下标从0开始,根据索引定位标签
    a_10 = locator.nth(9)

    # 获得标签中的href属性值和文本内容
    print(a_10.get_attribute('href'), a_10.inner_text())
    print('---------------------------------------------------------------------------')
    # 获得每一个a标签中的文本内容和href属性值
    for index in range(count):
        ele = locator.nth(index)
        text = ele.inner_text()
        href = ele.get_attribute('href')
        print(text, href)

    page.close()
    context.close()
    bro.close()






