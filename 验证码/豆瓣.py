from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from logeer import logger
username='123432421'
password='12341234214'
url=r'https://www.douban.com/'
chrome=webdriver.Chrome()
chrome.get(url)
wait=WebDriverWait(chrome,5)
#切换到登录子页面
chrome.switch_to.frame(chrome.find_element_by_xpath('//div[@class="login"]//iframe'))
p_u=wait.until(EC.presence_of_element_located((By.XPATH,'//li[@class="account-tab-account"]'))).click()
user=chrome.find_element_by_css_selector('#username')
user.clear()
time.sleep(random.random())
user.send_keys(username)
passs=chrome.find_element_by_css_selector('#password')
passs.clear()
time.sleep(random.random())
passs.send_keys(password)
login=chrome.find_element_by_css_selector('div.account-form-field-submit > a')
time.sleep(random.random())
login.click()
time.sleep(3)
if wait.until(EC.title_is('豆瓣')):
    logger.info('登陆成功')
else:
    try:
        chrome.switch_to.frame(chrome.find_element_by_xpath('//*[@id="TCaptcha"]/iframe'))
        time.sleep(3)
        img=chrome.find_element_by_xpath('//*[@id="slideBlock"]')
        print(img.location)
        print(img.size)
    except Exception:
        pass




