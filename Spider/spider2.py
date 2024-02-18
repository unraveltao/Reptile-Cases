# 搜狗简易网页采集器
import requests
#请求参数动态化
keyword = input('请输入关键字:')
#如果请求失败，那就是模仿的力度不够，第一次我未加请求头中的headers,导致搜索404
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
#稍后想要把该字典作为请求参数
#params参数就是用来在请求时携带指定的请求参数
#query是由多次搜索，后发现的不变的响应数据   开发者工具-->网络-->负载
params = {
    'query':keyword, #只存在一个键值对（存在一组请求参数）
}
#1.指定url
url = 'https://www.sogou.com/web' #需要将请求参数去除
#2.发起请求
#params参数就是用来在请求时携带指定的请求参数
response = requests.get(url=url,headers=headers,params=params)

#3.获取响应数据
page_text = response.text

#4.持久化存储
fileName = keyword + '.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)