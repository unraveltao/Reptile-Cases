#肯德基:将餐厅的位置信息进行数据爬取(动态加载数据)
import requests
headers = { #存放需要伪装的头信息UA检测
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
#post请求的请求参数
data = {
    "cname": "",
    "pid": "",
    "keyword": "天津",
    "pageIndex": "1",
    "pageSize": "10",
}
#在抓包工具中：Form Data存放的是post请求的请求参数，而Query String中存放的是get请求的请求参数
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#在post请求中，处理请求参数的是data这个参数不是params
response = requests.post(url=url,headers=headers,data=data)
#将响应数据进行反序列化
page_text = response.json()    #在preview(预览)种，判断数据类型JSON-->
# {Table: [{rowcount: 18080}],…}
# Table:[{rowcount: 18080}]
# Table1: [{rownum: 111, storeName: "平度帝王餐厅", addressDetail: "平度市李园街道缔王广场肯德基（红旗路164号）", pro: "礼品卡",…},…]
for dic in page_text['Table1']:
    name = dic['storeName']
    addr = dic['addressDetail']
    rownum = dic['rownum']
    print(rownum,name,addr)