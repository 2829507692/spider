import requests
from PIL import Image
from io import BytesIO
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.headers)
# print(r.json())
# print(r.text)

# payload = {'key1': 'value1', 'key2': '嘿嘿','key3':[1,2,3,4,]}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)

r=requests.get('http://pic40.nipic.com/20140331/9469669_142840860000_2.jpg')
i = Image.open(BytesIO(r.content))
print(i)