#彼岸图网：美女图片爬取
import requests
from lxml import etree
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
for page in range(1,6):
    if page == 1:
        new_url = 'https://pic.netbian.com/4kmeinv/index.html'
    else:
        new_url = format(url%page)
    print('----------正在请求下载第%d页的图片数据----------'%page)
    response = requests.get(url=new_url,headers=headers)
    response.encoding ='gbk'
    page_text = response.text
    tree = etree.HTML(page_text)

    list_li = tree.xpath('//div[@class="slist"]/ul/li')
    for li in list_li:
        #局部解析:将li标签中指定的内容解析出来
        img_title = li.xpath('./a/b/text()')[0] + '.jpg'
        img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]

        img_data = requests.get(img_src).content
        img_path = 'girl/' + img_title
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(img_path,'successfully downloaded')