import selenium
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time
import random

url='https://www.zhihu.com/signin?'
chrome=selenium.webdriver.Chrome()
wait=WebDriverWait(chrome,5)
chrome.get(url)

def sleep_time():
    ret=time.sleep(random.random())
    return ret


def show_image(top,buttom,left,rirht):
    screen =chrome.save_screenshot('yzm.png')
    img=Image.open('yzm.png')
    screen.crop(top,buttom,left,rirht)
    screen.show()


def login():
    username=chrome.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
    password=chrome.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
    sleep_time()
    username.send_keys('####')
    sleep_time()
    password.send_keys('####')
    sleep_time()
    button=chrome.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
    sleep_time()
    button.click()
    img=wait.until(Ec.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/span/div/img')))
    # img=chrome.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/span/div/img')
    ###验证位置
    location=img.location
    size=img.size
    top,buttom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
    print('验证码位置',top,buttom,left,right)
    show_image(top,buttom,left,right)
    chrome.quit()

if __name__ == '__main__':
    login()