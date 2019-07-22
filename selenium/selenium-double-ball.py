from selenium import webdriver
from lxml import etree
import time
num=input('请输入你要查询的期数')
#//td/a[not(@title)]
url='http://datachart.500.com/ssq/?expect=%s'%int(num)
chrome=webdriver.Chrome()
chrome.get(url)
ret=chrome.page_source
time.sleep(10)
e=etree.HTML(ret)
datas=e.xpath("//tbody[@id='tdata']//tr[not(@class)]//td[@align='center']/text()")
balls=e.xpath("//tbody[@id='tdata']//tr[not(@class)]")
info=zip(datas,balls)
for data ,ball in info:
    red_ball='-'.join(ball.xpath('./td[@class="chartBall01"]/text()'))
    blue_ball=ball.xpath('./td[@class="chartBall02"]/text()')[0]
    print(data,red_ball,blue_ball)
chrome.quit()