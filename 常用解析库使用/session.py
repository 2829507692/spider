import requests
import urllib3
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
# res =s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(res.text)


# 任何你传递给请求方法的字典都会与已设置会话层数据合并。方法层的参数覆盖会话的参数。
#
# 不过需要注意，就算使用了会话，方法级别的参数也不会被跨请求保持。
urllib3.disable_warnings()#禁用安全警告
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'