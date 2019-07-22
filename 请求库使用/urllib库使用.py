#! /usr/bin/env python基础
# -*- coding: utf-8 -*-

from urllib import request

res =request.urlopen(url='http://baidu.com')
print(res.read())

#下载;
request.urlretrieve('https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/17267/1.jpg','mz.jpg')

#解析连接
from urllib import parse

data ={'ha':'nb'}
#编码
url ='http//:www.baidu.com?'+parse.urlencode(data)
print(url)
#解码
res = parse.parse_qs(url)
print(res)

#分割url

url ='https://www.baidu.com/s?tn=44004473_oem_dg&ie=UTF-8&wd=%E9%87%91%E5%A4%A7%E5%B7%9D%E6%98%A5%E5%A4%8F%E7%83%AD%E6%81%8B'
res =parse.urlsplit(url)
print(res)
ress =parse.urlparse(url)
print(ress)