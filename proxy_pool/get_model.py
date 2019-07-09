import json
from pyquery import PyQuery as P
from fake_useragent import UserAgent
import requests
headers={
    'User-Agent':UserAgent().random
}

class ProxyMeta(type):
    def __new__(cls,name,bases,attrs):
        count=0
        attrs['_CrawlFunc_']=[]
        for k,v  in attrs.items():
            if 'crawl' in k:
                attrs['_CrawlFunc_'].append(k)
                count +=1
        attrs['_CrawCount_']=count
        return type.__new__(cls,name,bases,attrs)


class Crawler(object,metaclass=ProxyMeta):
    def get_profies(self,callback):
        '''
        :param callback:
        :return:返回代理列表
        '''
        proxies=[]
        for proxy in eval('self.{}()'.format(callback)):
            print('成功取到代理：',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_kuaidaili(self,page_count=5):
        '''
        :param page_count:
        :return: yiled 一个一个的代理
        '''
        url_list = ['https://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(1, page_count)]
        for url in url_list:
            doc = P(requests.get(url, headers=headers).text)
            items = doc('tbody>tr').items()
            for tr in items:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_nimadaili(self,page_count=5):
        '''
        :param page_count:
        :return: yiled 一个一个的代理
        '''
        url_list = ['http://www.nimadaili.com/gaoni/{}'.format(i) for i in range(1, page_count)]
        for url in url_list:
            doc = P(requests.get(url, headers=headers).text)
            items = doc('.fl-table>tbody>tr').items()
            for tr in items:
                proxy = tr.find('td:nth-child(1)').text()
                yield proxy

