from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains

username = 'username'
password = 'password'
url = r'https://www.douban.com/'
chrome = webdriver.Chrome()
chrome.get(url)
wait = WebDriverWait(chrome, 5)


def get_move(track):
    slide=chrome.find_element_by_css_selector('#slideBlock')
    for de in track:
        ActionChains(chrome).click_and_hold(slide).move_by_offset(de,0).perform()
        time.sleep(0.1)
    ActionChains(chrome).release().perform()


def get_track(distance):
    print(distance)
    #位移列表
    track=[]
    #初始位移
    current=0

    #减速阈值
    mid=distance*4/5

    #计算间隔
    t=0.2

    #初始速度
    v=0

    while current<distance:
        if current<mid:
            a=12
        else:
            a=-15
        #初速度
        v0=v
        #当前速度
        v=v0+a*t
        #移动距离
        x=v0*t+1/2*a*t*t
        #当前位移
        current += x
        print(x)
        track.append(x)
    get_move(track)

def get_distance(res):
    if res.get('err_no') == 0:
        groups = res.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        distance=locations[0][0]-locations[1][0]
        get_track(abs(distance))


def main():
    # 切换到登录子页面
    chrome.switch_to.frame(chrome.find_element_by_xpath('//div[@class="login"]//iframe'))
    p_u = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="account-tab-account"]'))).click()
    user = chrome.find_element_by_css_selector('#username')
    user.clear()
    time.sleep(random.random())
    user.send_keys(username)
    passs = chrome.find_element_by_css_selector('#password')
    passs.clear()
    time.sleep(random.random())
    passs.send_keys(password)
    login = chrome.find_element_by_css_selector('div.account-form-field-submit > a')
    time.sleep(random.random())
    login.click()
    time.sleep(5)
    chrome.switch_to.frame(chrome.find_element_by_xpath('//*[@id="TCaptcha"]/iframe'))
    time.sleep(5)
    code = chrome.find_element_by_css_selector('#slideBkg')
    code.screenshot('code.png')
    Chaojiying = Chaojiying_Client(username='cjyuser', password='cjypwd', soft_id=901074)
    img = code.screenshot_as_png
    res = Chaojiying.PostPic(img, 9102)
    print(res)
    get_distance(res)
    time.sleep(500)
    chrome.quit()
if __name__ == '__main__':
    main()