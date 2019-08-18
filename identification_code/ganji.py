from time import sleep
from random import random
from selenium import webdriver
from chaojiying import Chaojiying_Client
from PIL import Image
chaojiying_user='##'
chaojiying_pwd='##'
soft_id='899954'
url='https://passport.ganji.com/login.php?next=/'
class ganji():
    def __init__(self):
        self.chrome=webdriver.Chrome()
        self.Chojiying_client=Chaojiying_Client(username=chaojiying_user,
                                                password=chaojiying_pwd,soft_id=soft_id)
        self.user='user'
        self.password='pwd'

    def chrome_sleep(self):
        sleep(random())

    def login(self):
        self.chrome.get(url)
        first_title=self.chrome.find_element_by_xpath("//head/title")
        # print(first_title)
        input_user=self.chrome.find_element_by_css_selector('.usename')
        input_pwd=self.chrome.find_element_by_css_selector('.usepassword')
        self.chrome_sleep()
        input_user.send_keys(self.user)
        self.chrome_sleep()
        input_pwd.send_keys(self.password)
        button_login=self.chrome.find_element_by_css_selector('.submit')
        self.chrome_sleep()
        button_login.click()
        sleep(3)
        new_title=self.chrome.find_element_by_xpath("//head/title")
        # print(new_title)
        if first_title != new_title:
            print('不需要验证就可以登陆 嘿嘿！！！')
            return self.chrome
        code=self.get_code()
        input_code = self.chrome.find_element_by_css_selector('#login_checkcode_input')
        input_code.send_keys(str(code))
        sleep(2)
        button_login.click()
        sleep(5)
        new_title = self.chrome.find_element_by_xpath("//head/title")
        if first_title != new_title:
            print('登陆成功 嘿嘿！！！')
            return self.chrome
        else:
            self.login()
    def get_code(self):
        img=self.chrome.find_element_by_xpath("//div[@class='form-div js-checkcode']//img[@class='login-img-checkcode']")
        img=img.screenshot_as_png
        yzm=self.Chojiying_client.PostPic(im=img,codetype=1902)
        code=yzm.get('pic_str')
        return code

if __name__ == '__main__':
    ganji().login()