'''
实例
# 将生成图片尺寸设置为:320x240
curl 'http://localhost:8050/render.png?url=http://domain.com/page-with-javascript.html&width=320&height=240'
'''
import requests
url='https://www.jd.com/'
slpash_url='http://192.168.8.101:8050/render.png?url=%s&timeout=20&wait=0.5&width=320&height=240'%url
res=requests.get(slpash_url)
with open('1.png','wb') as fb:
    fb.write(res.content)