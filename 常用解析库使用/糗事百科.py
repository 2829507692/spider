import requests
import re
from fake_useragent import UserAgent
headers={
    'User-Agent':UserAgent().chrome
}
url ='https://www.qiushibaike.com/text/'
res=requests.get(url,headers=headers)
rep =re.findall(r'<div.*?content.*?span>\s+(.*?)\s+</span.*?',res.text,re.S)
for i in rep:
    print(i+'\n\n')
