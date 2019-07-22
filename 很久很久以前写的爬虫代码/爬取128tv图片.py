import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import os
def gethtml(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'lxml')
    sus = soup.select('.list a')
    return sus
def getjpg(sus):
    try:
        for su in sus:
            print(su['href'],su.span.string)
            paths = 'E://%s//%s//'%('图片',su.span.string)
            if os.path.exists(paths)==False:
                os.makedirs(paths)
            url = 'https://www.705hs.com/%s'%su['href']
            ps =requests.get(url)
            ps.encoding=ps.apparent_encoding
            soups=BeautifulSoup(ps.text,'lxml')
            sps=soups.select('.conttxt img')
            for i,sp in enumerate(sps):
                print(i,sp['src'])
                ull= sp['src']
                uls=requests.get(ull)
                with open(paths + str(i) + '.jpg', 'wb') as file:
                    try:
                        file.write(uls.content)
                        file.close()
                    except:
                        print('错误')
                    finally:
                        print('第%s张完成' % i)
    except:
        print('请求错误')
def main(i):
    url = 'https://www.705hs.com/Html/63/index-%s.html' % i
    sus = gethtml(url)
    getjpg(sus)
    print('完成')
if __name__ == '__main__':
    with Pool(20) as p:
        p.map(main, range(2, 20))

