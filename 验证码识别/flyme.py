url='https://login.flyme.cn/sso?appuri=&useruri=http%3A%2F%2Fstore.meizu.com%2Fmember%2Flogin.htm%3Fuseruri%3Dhttp%3A%2F%2Fwww.meizu.com&sid=unionlogin&service=store&autodirct=true'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.support import expected_conditions as ec
from chaojiying import Chaojiying_Client
class ZhipinSpider(object):
    def __init__(self):
        self.url=url
        self.chrome=webdriver.Chrome()
        self.username='user'
        self.pwd='pwd'
        script='''
        window.navigator.webdriver=undefined
        '''
        self.chrome.execute_script(script)
        self.Chaojiying=Chaojiying_Client(username='cjyuser',password='cjypwd',soft_id=901069)

    def start(self):
        print('默认滑动验证码')
        self.chrome.get(self.url)
        time.sleep(5)
        user=self.chrome.find_element_by_css_selector('.ipt-account')
        user.send_keys(self.username)
        pwd=self.chrome.find_element_by_css_selector("[type='password']")
        pwd.send_keys(self.pwd)
        btu=self.chrome.find_element_by_css_selector('.geetest_btn')
        btu.click()
        time.sleep(5)
        t=self.chrome.find_element_by_css_selector('.geetest_success_radar_tip_content')
        if t.text=='验证成功':
            print('不需要进行验证码')
        else:
            try:
                code=self.chrome.find_element_by_css_selector('div.geetest_wrap')
                print(code.location)
                code.screenshot('code.png')
            except:
                print('该验证码为点击验证码')
                code=self.chrome.find_element_by_css_selector('div.geetest_silver')
                code.screenshot('code.png')
                img =code.screenshot_as_png
                result=self.Chaojiying.PostPic(img,9004)
                print(result)
                self.get_point(result,code)

    def get_point(self,result,img_obj):
        if result.get('err_no')==0:
            ''.split()
            groups=result.get('pic_str').split('|')
            locations=[[int(number)for number in group.split(',')]for group in groups]
            print(locations)
            self.touch(locations,img_obj)

    def touch(self,locations,img_obj):
        for location in locations:
            ActionChains(self.chrome).move_to_element_with_offset(img_obj,location[0],location[1]).click().perform()
            time.sleep(random.random())

        commit_button=self.chrome.find_element_by_css_selector('.geetest_commit_tip')
        commit_button.click()
        t=self.chrome.find_element_by_css_selector('.geetest_success_radar_tip_content')
        time.sleep(5)
        if t.text=='验证成功':
            print('检验成功')
            self.login()
        time.sleep(5000)

    def login(self):
        login_button=self.chrome.find_element_by_css_selector('.fullBtnBlue')
        login_button.click()
        time.sleep(5)
        if ec.title_contains('魅族官网 - 魅族 16Xs 手机,极边全面屏 三摄长续航'):
            print('登录成功')


    def __del__(self):
        self.chrome.quit()

if __name__ == '__main__':
    ZhipinSpider().start()