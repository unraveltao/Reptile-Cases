#小说碧血剑爬取，基于bs4对数据解析
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
           }

url = 'https://bixuejian.5000yan.com/'
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_test = response.text
#首页页面进行数据解析
soup = BeautifulSoup(page_test, 'lxml')
#定位所有a标签，保存到a_list中
a_list = soup.select('.paiban > li > a')
for a in a_list:
    # 章节的标题
    title = a.string         #提取数据
    # 章节详情页的url
    detail_url = a['href']   #提取标签属性值
    detail_response = requests.get(url=detail_url, headers=headers)
    detail_response.encoding = 'utf-8'
    detail_response_page = detail_response.text
    #详情页面进行数据解析
    detail_soup = BeautifulSoup(detail_response_page, 'lxml')
    div_tad = detail_soup.find('div',class_='grap')
    #章节内容
    content = div_tad.text
    file_name = 'novel' + title + '.txt'  #字符拼接  novel章节1.txt
    with open(file_name, 'w',encoding='utf8') as fp:
        fp.write(title+'\n'+content)
    print(title,':successful')
