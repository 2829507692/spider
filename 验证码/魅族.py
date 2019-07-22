from selenium import webdriver
from PIL import Image
from selenium.common.exceptions import TimeoutException
from logeer import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import chaojiying

chrome=webdriver.Chrome()
user='###'
wd='###'
wait=WebDriverWait(chrome,5)
url='https://login.flyme.cn/'
chrome.get(url)

user_input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#account')))
user_input.send_keys(user)

pass_input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#password')))
pass_input.send_keys(wd)

chrome.implicitly_wait(2)
chrome.find_element_by_xpath("//div[@class='geetest_wait']").click()


button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login'))).click()

def fet_img():
    sleep(5)
    img=chrome.find_element_by_css_selector('.geetest_item_img')
    print(img.location,img.size)
    image=img.screenshot_as_png
    l=chaojiying.Chaojiying_Client(username=####,password='#####').PostPic(image,1901)
    with open('1.png','wb') as f:
        f.write(image)
    print(l)

if chrome.title=='账号管理':
    logger.info('恭喜你登陆成功！！！')
else:
    logger.warning('登录失败！！！')
    fet_img()
chrome.quit()

