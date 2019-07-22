from fake_useragent import UserAgent
import requests
import re
import time
url='https://passport.ganji.com/login.php?'
headers={
    'User-Agent':UserAgent().random
}
resquest=requests.Session()
response=requests.get(url=url,headers=headers).text
hashcode = re.search(r'"__hash__":"(.*?)"}',response).group(1)
url = 'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha'
res = resquest.get(url).content
with open('yzm.jpg', 'wb')as f:
    f.write(res)
    f.flush()
time.sleep(2)
yzm= input('请输入验证码>>>')
peramas={
    'username': 'love2c133',
    'password': 'f5317355',
    'setcookie': '14',
    'checkCode': yzm,
    'next': '/',
    'source': 'passport',
    '__hash__': hashcode
}
ret= resquest.post(url=url,data=peramas)
print(ret.text)

