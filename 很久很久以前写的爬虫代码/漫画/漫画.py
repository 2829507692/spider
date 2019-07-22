
from urllib.parse import urlencode

import requests

from pyquery import PyQuery as py

import os

from config import *

import re

from multiprocessing import Pool



def get_one_page(ID,id):
    data = {'comicid' :ID,
            'chapterid' :id}
    url = 'http://www.manhuadao.cn/Comic/ComicView?' + urlencode(data)
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=head)
        response.encoding=response.apparent_encoding
        return response.text
    except:
        print('请求错误:',url)

def get_page_info(html):
    try:
        doc = py(html)
        urs = doc('body > div.read-core > div.center-t > div > ul [style] img').items()
        capital = doc('#top > h1 > span').text()[1:]
        print(capital)
        name = doc('#top > h1 > a:nth-child(2)').text()[1:]
        for n,url in enumerate(urs):
            s = url.attr('src')
            write_info(name,s,capital,n)
    except:
        print('请求错误')

def write_info(name,s,capital,n):
    pathss =path +name+ '/'+capital
    try:
        if os.path.exists(pathss) == False:
            os.mkdir(pathss)
        image = requests.get(s).content
        if os.path.exists(pathss+'/'+ str(n)+'.jpg') ==False:
            with open( pathss+'/'+ str(n)+'.jpg','wb') as f:
                f.write(image)
                f.close()
    except:
        print('此张请求错误')
    finally:
        print('%s%s第%s张完成'%(name,capital,str(n)))

def main(i):
        html =get_one_page(ID,i)
        get_page_info(html)

if __name__ =='__main__':
    url = 'http://www.manhuadao.cn/Home/ComicDetail?'
    urls = url + urlencode({'id': ID})
    doc = py(requests.get(urls).text)
    name = doc('#evaluation > section > section > div.book-detail > div.detail-item > div.title > h2').text()
    print(name)
    paths = path + name
    if os.path.exists(paths) == False:
        os.mkdir(paths)
    start_pages = doc('#evaluation > section > section > div.book-detail > div.radios > div > a').attr('href')
    start_page = start_pages[-7:]
    pages = doc('#evaluation > section > div.detail-content > section > div.title > span.title-sub').text()
    page = re.search('\d+', pages).group(0)

    with Pool(10) as p:
        p.map(main,range(int(start_page),int(start_page)+int(page)))