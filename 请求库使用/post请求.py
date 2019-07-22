from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

# url = 'http://www.52studyit.com/member.php?mod=logging&action=login&' \
#       'loginsubmit=yes&handlekey=login&loginhash=LDI9v&inajax=1'
# data = {
#     'username': 'f5317355',
#     'password': 'Ff5317355'
# }
# headers={
#     'User-Agent':UserAgent().chrome
# }
# request=Request(url,headers=headers,data=urlencode(data).encode())
# res=urlopen(request)
# print(res.read().decode())
# import requests
base_url = 'http://blog.sxt.cn/wp-admin/admin-ajax.php?action=ajax_login'
data={
    'username': '17703181473',
    'password': '123456'
}
# res =requests.post(base_url,json=data)
# print(res)
headers={'User-Agent':UserAgent().chrome}
request =Request(base_url,data=urlencode(data).encode('utf-8'),headers=headers)
res =urlopen(request)
print(res.read().decode('utf-8'))



