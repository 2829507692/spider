#龙武帝尊爬取
import requests
from bs4 import BeautifulSoup
import re
import lxml
import os
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
    }
r = requests.get('https://xs.sogou.com/list/7727651310',headers=header)
pattern = re.compile('<li.*?c3.*?href="(.*?)".*?span>(.*?)</span.*?li>',re.S)
sus= re.findall(pattern,r.text)
for su in sus:
    url = 'https://xs.sogou.com/%s'%su[0]
    rr =requests.get(url).text
    soup = BeautifulSoup(rr,"lxml")
    ps= soup.select('#contentWp p')
    with open('F://'+'龙武帝尊.txt','a') as fil:
            fil.write(str(su[1])+'\n')
    for p in ps:
        with open('F://'+'龙武帝尊.txt','a') as file:
            file.write(p.string+'\n')
    print('第%s章下载完成'%su[1])
print('下载完成')
            
