#彼岸图网：美女动漫图片爬取
import requests
from lxml import etree
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
"""
    第一页    http://pic.netbian.com/4kdongman/
    第二页    https://pic.netbian.com/4kdongman/index_2.html
    第三页    https://pic.netbian.com/4kdongman/index_3.html
"""
for page in range(1,11):
    #第一页与其他页url不同
    if page == 1:
        url = 'http://pic.netbian.com/4kdongman/'
    else:
        url = f'http://pic.netbian.com/4kdongman/index_{page}.html'
    print(f'------------------------正在下载{page}图片------------------------')
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    #数据解析:图片地址+图片名称
    tree = etree.HTML(page_text)
    """
        HTML()专门用来解析网络请求到的页面源码数据
        该列表中存储的是每一个li标签
        xpath的返回值是列表，根据索引取值
    """
    #全局解析
    list_li = tree.xpath('//div[@class="slist"]/ul/li')
    for li in list_li:
        #局部解析:将li标签中指定的内容解析出来
        img_title = li.xpath('./a/b/text()')[0] + '.jpg'  #xpath的返回值是列表
        img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        """
        对网页进行分析，src的值没有域名
        print(img_title,img_src)   
        发现乱码utf-8不行，用gbk
        对图片发起请求，存储图片数据
        """
        img_data = requests.get(img_src).content
        img_path = 'pic/' + img_title
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(img_path,'successfully downloaded')