from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
from pyquery import PyQuery as p
import pymongo

def save_mongo(product):
    host='127.0.0.1'
    port=27017
    client=pymongo.MongoClient(host,port)#创建一链接
    db=client.taobao
    collection=db.info
    collection.insert(product)

def add_cookise():
    with open('cookies.json') as f:
        str_pbj=json.load(f)
        for i in str_pbj:
            browser.add_cookie(i)
def start_page():
    inputlb=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
    button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    inputlb.clear()
    inputlb.send_keys(keywords)
    button.click()
def page_parser(page):
    while True:
        current=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active>span'))).text
        print('当前正在爬取第{}页'.format(current))
        buttom = browser.find_element_by_css_selector('li.item.next a')
        buttom.click()
        if int(current)<=page:
            html =p(browser.page_source)
            items=html('#mainsrp-itemlist .items .item').items()
            for item in items:
                product={
                    'img':item.find('.pic .img').attr('data-src'),
                    'price':item.find('.price').text(),
                    'deal':item.find('.deal-cnt').text(),
                    'shop':item.find('.shop').text(),
                    'location':item.find('.location').text()
                }
                print(product)
                save_mongo(product)
                time.sleep(3)
        else:
            break

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    # browser.implicitly_wait()指定等待时间
    # keywords = input('请输入你要搜索的商品名')
    # page=int(input('请输入你要查询的页码数'))
    page = 5
    keywords='平板'
    wait=WebDriverWait(browser,10)
    add_cookise()
    start_page()
    page_parser(page)
    browser.quit()