import requests
import json
import csv
from pyquery import PyQuery
url='https://www.zhihu.com/explore'
headers={'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
res =requests.get('https://www.zhihu.com/explore',headers=headers)
doc=PyQuery(res.text)
items=doc('div.explore-feed.feed-item').items()
# with open('zhihu.csv','w',encoding='utf-8') as f:
#     # writer=csv.writer(f)
#     fieldname = ['title', 'author', 'answer']
#     writer = csv.DictWriter(f,fieldnames=fieldname)
#     for item in items:
#         title=item('h2').text()
#         author=item.find('.author-link').text()
#         answer=item.find('div.zh-summary.summary.clearfix').text()
#         #写入文本
#         # file=open('zhihu.txt','a',encoding='utf-8')
#         # file.write('\n'.join([title,author,answer]))
#         # file.write('\n'+'*'*50+'\n')
#         # file.close()
#         #写入json
#         obj={
#             "title":title,
#             'author':author,
#             'answer':answer
#         }
#         # json.dump(obj,f,ensure_ascii=False)
#         #写入csv
#         # writer.writerow([title,author,answer])
#         writer.writerow(obj)

#csv读取
with open('zhihu.csv','r',encoding='utf-8') as f:
    reder=csv.reader(f)
    for i in reder:
        print(i)