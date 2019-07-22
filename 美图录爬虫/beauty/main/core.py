import os
import sys
import requests
from pyquery import PyQuery as pq
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import re

paths = os.path.dirname(os.getcwd())
sys.path.append(paths)
from src.path import path

# my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14","Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"	]
# use_agent=random.choice(my_headers)
use_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'


def img_writen(name, url, pathes):
    headers = {'user - agent': use_agent, 'referer': 'https://www.meitulu.com/t/xiuren/'}
    content = requests.get(url=url, headers=headers)
    print(content.status_code)
    with open(pathes + name + '.jpg', 'wb') as f:
        f.write(content.content)
        f.close()


def every_photo_url(url_list, pathes):
    start_url = 'https://www.meitulu.com/img.html?'
    for url in url_list:
        headers = {'user - agent': use_agent}
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        doc = pq(response)
        img_list = doc('.content > center img').items()
        # print(img_list)
        for i in img_list:
            imgurl = i.attr('src')
            name = i.attr('alt')
            print(name, imgurl)
            img_writen(name, imgurl, pathes)


def one_url_parser(url):  # 分析套图的url
    headers = {'user - agent': use_agent}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    doc = pq(response)
    ret1 = doc('body > div.width > div.c_l > p:nth-child(3)').text()
    ret2 = doc('body > div.width > div.weizhi > h1').text()
    url_list = []
    url_list.append(url)
    print(ret2, '------>', ret1)  # *********
    pathes = path + ret2 + '//'
    if os.path.exists(pathes):
        return
    else:
        os.makedirs(pathes)
    num = int(re.search(r'\d+', ret1).group(0))
    num, raim = divmod(num, 4)
    # print(num,raim)
    for i in range(num):
        par_str = '_' + str(i + 2)
        s = url.split('.')
        s[-2] = s[-2] + par_str
        parser_url = '.'.join(s)
        url_list.append(parser_url)
    # print(url_list)
    every_photo_url(url_list, pathes)


def url_parser(url):  # 分析共有多少页，及获得每页的连接
    headers = {'user - agent': use_agent}
    url_list = []
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    doc = pq(response)
    res = doc('#pages > a:nth-child(1)')
    num = int(re.search(r'\d+', res.text()).group(0))  # 求出url所包含的所有套图
    # print(num)
    page = divmod(int(num), 60)[0]  # 求出所有页数
    # print(page)
    url_list.append(url)
    if page == 0:
        return url_list
    else:
        for i in range(2, page + 2):
            # print(i)
            url_paser = url + str(i) + '.html'  # 拼接形成页数链接
            url_list.append(url_paser)
        return url_list


def get_url(url):  # 爬取一个页面所有的套图链接
    first_list = []
    headers = {'user - agent': use_agent}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    doc = pq(response)
    ret = doc('.boxs > .img li>a')
    for url in ret.items():
        # print('\n'+url.attr('href'),url('img').attr('alt'))
        first_list.append(url.attr('href'))
    return first_list


def main():
    start_url = 'https://www.meitulu.com/'
    headers = {'user - agent': use_agent}
    response = requests.get(url=start_url, headers=headers).text
    doc = pq(response)
    res = doc('.model_source > ul li a').items()
    url_dic = {}
    for index, url in enumerate(res):
        print(index, '----->', url.text(), url.attr('href'))
        url_dic.setdefault(index, url.attr('href'))
    choise = int(input('请输入相应序号>>>:'))
    page_url_list = url_parser(url_dic[choise])
    # print(page_url_list)
    demo_url_list = []
    pool = ThreadPoolExecutor(max_workers=20)
    process_pool = Pool(5)
    for i in page_url_list:
        p = process_pool.apply_async(func=get_url, args=(i,))
        demo_url_list.append(p)
    process_pool.close()
    process_pool.join()
    for p in demo_url_list:
        p_list = p.get()
        for i in p_list:
            pool.submit(one_url_parser, i)
    pool.shutdown()
    # test='https://www.meitulu.com/item/17267.html'#测试
    # one_url_parser(test)


if __name__ == '__main__':
    main()
