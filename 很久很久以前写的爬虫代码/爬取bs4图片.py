import requests
import re
import lxml
import os
from bs4 import BeautifulSoup
heaer = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
         }
response = requests.get('http://www.btshoufa.net/forum-52-1.html').text
pattern = re.compile('<tbody.*?normalthread_.*?href="(.*?)".*?atarget.*?xst">(.*?)</a>',re.S)
result = re.findall(pattern,response)
for li in result:
    url = 'http://www.btshoufa.net/%s'%li[0]
    paths = 'F://%s//'%li[1]
    if os.path.exists(paths) ==False:
        os.makedirs(paths)
    ru = requests.get(url,headers = heaer)
    ru.encoding=ru.apparent_encoding
    rus=ru.text
    soup = BeautifulSoup(rus,'lxml')
    sus = soup.select('.t_f img')
    for i,su in enumerate(sus):
        try:
            ss = su['file']
            rs = requests.get(ss)
            with open(paths+str(i)+'.jpg','wb') as f:
                f.write(rs.content)
                f.close()
        except:
            ''
        finally:
            print('第%d张'%i)
        
print('打印完成')
