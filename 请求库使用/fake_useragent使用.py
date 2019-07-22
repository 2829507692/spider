from fake_useragent import UserAgent
s=UserAgent()
print(s.chrome)
print(s.ie)
print(s.edge)
print(s.firefox)
#
#
# import requests
# headers={
# 'User-Agent':s.chrome
# }
# requests.get('http:..www.baidu.com',headers=headers)