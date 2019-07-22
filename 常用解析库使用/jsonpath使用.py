from jsonpath import jsonpath
import requests
url='https://www.toutiao.com/stream/widget/local_weather/city/'
res=requests.get(url)
pro=jsonpath(res.json(),'$..data')
print(type(pro))
for i in  pro:
    for j in i:
        print(j,i[j])