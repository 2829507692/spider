from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler
import requests
url ='http://httpbin.org/get'
header={'User-Agent':UserAgent().chrome}
request=Request(url,headers=header)
#不加密代理写法
hander=ProxyHandler({'http':'171.83.167.131:9999'})
# #加密代理写法
# # hander=ProxyHandler({'http':'username:password@171.83.167.131:9999'})
res=build_opener(hander).open(request)
print(res.read().decode('utf-8'))
# proxies={'http':'http://206.81.13.45:8080'}
#加密代理
#proxies = {"http": "http://user:pass@10.10.1.10:3128/",}
# res =requests.get(url,headers=header,proxies=proxies)
# print(res.text)
# 要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。
# proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}