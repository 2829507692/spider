from urllib.request import urlopen,Request
from fake_useragent import UserAgent
headers ={
    'User-Agent':UserAgent().chrome
}
try:
    url ='hhttp://www.sxt.cn/index/login/login.html'
    request =Request(url,headers=headers)
    res = urlopen(request)
    print(res.read().decode())
except URLError as e:
    print(e)





