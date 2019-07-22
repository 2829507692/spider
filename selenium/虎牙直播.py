import time
from selenium import webdriver
broswer=webdriver.Chrome()
broswer.get('https://www.huya.com/g/wzry')
html =broswer.page_source
flag=True
page_num = broswer.find_element_by_css_selector('.laypage_last').get_attribute('data-page')
with open('huya','w',encoding='utf-8') as f:
    while flag:
        time.sleep(5)
        title = broswer.find_elements_by_xpath('//a[@class="title new-clickstat"]')
        name = broswer.find_elements_by_xpath('//i[@class="nick"]')
        fans = broswer.find_elements_by_xpath('//span[@class="num"]/i[@class="js-num"]')
        s = zip(title, name, fans)
        cur = broswer.find_element_by_xpath('//span[@class="laypage_curr"]').text
        for title, name, fans in s:
            f.write(title.text + '    ' + name.text + '   ' + fans.text + '\n')
        if int(cur)==int(page_num):
            flag=False
            continue
        broswer.find_element_by_class_name('laypage_next').click()

    broswer.quit()
