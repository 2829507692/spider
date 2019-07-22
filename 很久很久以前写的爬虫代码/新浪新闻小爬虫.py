import requests
from fake_useragent import UserAgent
from lxml import etree
headers={
    'User-Agent':UserAgent().chrome
}
ret=requests.get(url='https://news.sina.com.cn/c/2019-05-15/doc-ihvhiqax8939548.shtml',headers=headers,)
ret.encoding='utf-8'
e=etree.HTML(ret.text)

title=e.xpath('//h1[@class="main-title"]/text()')
article=e.xpath('//div[@id="article"]//p')
for i in article:
    i=i.xpath('string(.)')
    print(i)
img_url=e.xpath('//div[@id="article"]//div[@class="img_wrapper"]/img/@src')
print(img_url)