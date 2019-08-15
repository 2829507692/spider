from urllib.parse import quote
import requests
from lxml import etree

lua='''
function main(splash)
  assert(splash:go('https://www.jd.com/'))
  local input= splash:select('#key')
  local button=splash:select('button.button')
  assert(input:send_text('iphone'))
  assert(button:mouse_click{y=5})
  assert(splash:set_viewport_full())
  assert(splash:wait(10))

  return splash:html()
end
'''
'''
//input[starts-with(@name,'name1')]     查找name属性中开始位置包含'name1'关键字的页面元素
//input[contains(@name,'na')]'''
lua=quote(lua)

splash='http://192.168.8.101:8050/execute?lua_source='+lua

res=requests.get(splash)
res.encoding='utf-8'
e=etree.HTML(res.text)
price=e.xpath("//div[@class='p-price']/strong/i/text()")
name=e.xpath("//div[contains(@class,'p-name')]/a/i/text()")
shop=e.xpath("//div[@class='p-shop']/span/a/text()")
for i in zip(name,price,shop):
    print(i)