from pyquery import PyQuery as py
urllist=py(url='https://book.qidian.com/info/1013408461#Catalog')
s = urllist.find('.volume>.cf>li>a').items()
paths = 'F://我真是个大魔王.txt'
for ss in s:
    print(ss.text())
    ur='http:%s'%ss.attr.href
    sus=py(ur)
    rus=sus.find('.main-text-wrap p').items()
    for ru in rus:
        try:
            with open(paths,'a') as f:
                f.write(ru.text()+'\n')
                f.close
        except:
            ''
    print('%s完成'%ss.text())
print('完成')
