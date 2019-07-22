from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl
#忽略证书
#第一种方法
# context = ssl._create_unverified_context()
# url ='https://www.12306.cn/index/index.html'
# headers= {'User-Agent':UserAgent().chrome}
# request = Request(url,headers=headers)
# res = urlopen(request,context=context)
# print(res.read().decode('utf-8'))
#第二种
import requests
res =requests.get('https://requestb.in',verify=False)
print(res)
#第三种
# verify指定证书路径
# 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径
# 如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理。

# 默认情况下， verify 是设置为 True 的。选项 verify 仅应用于主机证书。
# 对于私有证书，你也可以传递一个 CA_BUNDLE 文件的路径给 verify。你也可以设置 # REQUEST_CA_BUNDLE 环境变量。

