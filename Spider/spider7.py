#网易云歌曲
import requests
from lxml import etree

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
#1.请求歌手歌单页面
singer_url = input("请输入你想下载的歌手链接：")
"""
搜索url    https://music.163.com/#/playlist?id=2226970083
发送请求url    https://music.163.com/playlist?id=2226970083
"""
#对url处理
url = singer_url.replace('/#','')
response = requests.get(url=url, headers=headers)
#2.数据解析，筛选标签
tree = etree.HTML(response.text)
music_list = tree.xpath('//a[contains(@href, "/song?")]')

for music_label in music_list:
      href = music_label.xpath('./@href')[0]  # /song?id=1851022762
      music_id = href.split('=')[1]   #取出music的id值    1851022762,有的取不出id值
      music_name = music_label.xpath('./text()')[0]
      music_url = "https://music.163.com/song/media/outer/url?id=" + music_id
      music_response = requests.get(url=music_url, headers=headers)
      chapter = music_name + ".mp3"
      #异常处理
      try:
          with open(chapter, 'wb') as f:
             f.write(music_response.content)
             print("《%s》downlode" % music_name)
      except:
          break


