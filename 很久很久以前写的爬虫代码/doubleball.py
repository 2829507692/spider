from fake_useragent import UserAgent
import requests
from lxml import etree
import time
heasers={
    'User-Agent':UserAgent().chrome,
    'Connection': 'keep-alive'
}
params={
    'expect':100
}
#//td/a[not(@title)]
url='http://datachart.500.com/ssq/'
ret=requests.get(url=url,headers=heasers,params=params)
print(ret.url)
ret.encoding='utf-8'
e=etree.HTML(ret.text)
datas=e.xpath("//tbody[@id='tdata']//tr[not(@class)]//td[@align='center']/text()")
balls=e.xpath("//tbody[@id='tdata']//tr[not(@class)]")
info=zip(datas,balls)
for data ,ball in info:
    red_ball='-'.join(ball.xpath('./td[@class="chartBall01"]/text()'))
    blue_ball=ball.xpath('./td[@class="chartBall02"]/text()')[0]
    print(data,red_ball,blue_ball)
