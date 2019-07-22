from selenium import webdriver
from lxml import etree
import time
browser=webdriver.Chrome()
url='https://search.jd.com/Search?keyword=%E6%80%A7%E6%84%9F%E5%86%85%E8%A1%A3&enc=utf-8&wq=%E6%80%A7%E6%84%9F%E5%86%85%E8%A1%A3&pvid=a8faaac44dca4ad2bf1c3c2950101f93'
browser.get(url)
js='document.documentElement.scrollTop=8476'
browser.execute_script(js)
time.sleep(3)
ret=browser.page_source
e=etree.HTML(ret)
title=e.xpath('//li//div[@class="gl-i-wrap"]//div[@class="p-img"]//a/@title')
name=e.xpath('//li//div[@class="gl-i-wrap"]//div[@class="p-name p-name-type-2"]//a/em/text()')
for i in name:
    print(i)
browser.quit()