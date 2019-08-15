'''
实列
'http://localhost:8050/render.html?url=http://domain.com/page-with-javascript.html&timeout=10&wait=0.5'
'''
import requests
url='https://www.jd.com/'
slpash_url='http://192.168.8.101:8050/render.html?url=%s&timeout=20&wait=0.5'%url

res=requests.get(slpash_url).text
print(res)