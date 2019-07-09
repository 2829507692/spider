from pyquery import PyQuery as P
from fake_useragent import UserAgent
import requests
headers={
    'User-Agent':UserAgent().random
}
# url_list=['https://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(1,4)]
# for url in url_list:
#     doc = P(requests.get(url, headers=headers).text)
#     items = doc('tbody>tr').items()
#     for tr in items:
#         ip=tr.find('td:nth-child(1)').text()
#         port=tr.find('td:nth-child(2)').text()
#         print(ip,port)

url_list = ['http://www.nimadaili.com/gaoni/{}'.format(i) for i in range(1, 5)]
for url in url_list:
    doc = P(requests.get(url, headers=headers).text)
    items = doc('.fl-table>tbody>tr').items()
    for tr in items:
        ip = tr.find('td:nth-child(1)').text()
        print(ip)