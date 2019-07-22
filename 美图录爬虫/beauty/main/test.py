from urllib import parse
test='https://www.meitulu.com/item/17281.html'
s =test.split('.')
print(s)
s[-2]=s[-2]+'_2'
url='.'.join(s)
print(url)