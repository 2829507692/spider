from lxml import etree
import requests
from fake_useragent import UserAgent
headers={
    'User-Agent':UserAgent().chrome
}

url='https://www.qidian.com/all?chanId=21&subCateId=8'
res =requests.get(url,headers=headers,)
res.encoding='utf-8'
e=etree.HTML(res.text)
name=e.xpath('//h4/a/text()')
# print(name)
author=e.xpath('//p[@class="author"]/a[1]/text()')
# print()
info={}
for i in range(len(name)):
    info.setdefault(name[i],author[i])
print(info)
