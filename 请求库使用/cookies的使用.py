from fake_useragent import UserAgent
from urllib.request import urlopen,Request,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode
import requests
url ='https://www.douban.com/people/196193479/'
# headers={
#     'User-Agent':UserAgent().chrome,
#     'Cookie': 'll="118371"; bid=IMNGUgLgxqM; __utma=30149280.1408506100.1557240665.1557243315.1557335379.3; __utmc=30149280; __utmz=30149280.1557335379.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19619; ap_v=0,6.0; douban-profile-remind=1; dbcl2="196193479:8KfDObwV1Yo"; ck=5Bnh; __utmb=30149280.23.9.1557335924611'
# }
# headers={'User-Agent':UserAgent().chrome}
# log_url="https://accounts.douban.com/j/mobile/login/basic"
# data={
#     'name':'18573479912',
#     'password': 'f5317355',
#     'remember': 'true',
# }
# request=Request(log_url,headers=headers,data=urlencode(data).encode('utf-8'))
# res=urlopen(request)//
# hander=HTTPCookieProcessor()//保存登录过的cookies信息  res=build_opener(hander).open(request)//
# print(res.read().decode('utf-8'))

# res =requests.get('http://www.baidu.com')
# jar =res.cookies#返回对象为一个RequestsCookieJar，可把其作为请求参数
# print(jar.get_dict())
# r = requests.get(url, cookies=jar)
# r.text
# headers={
#     'User-Agent':UserAgent().chrome
# }
# cookies={
#     'Cookie': 'll="118371"; bid=IMNGUgLgxqM; __utma=30149280.1408506100.1557240665.1557243315.1557335379.3; __utmz=30149280.1557335379.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19619; ap_v=0,6.0; douban-profile-remind=1; dbcl2="196193479:WacJKfHdDMY"; ck=u-TE; __utmc=30149280; __utmt=1; __utmb=30149280.52.9.1557338465228'
#
# }
# r=requests.get(url,headers=headers,cookies=cookies)
# print(r.text)
