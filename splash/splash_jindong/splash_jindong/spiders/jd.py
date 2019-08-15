# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy_splash import SplashRequest
import time
lua = '''
function main(splash,args)
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  local input= splash:select('#key')
  local button=splash:select('button.button')
  assert(input:send_text(args.keywords))
  assert(button:mouse_click{y=5})
  assert(splash:wait(args.wait))
  assert(splash:set_viewport_full())
 js=string.format("document.querySelector('input.input-txt:nth-child(2)').value=%d;document.querySelector('a.btn.btn-default:nth-child(4)').click()",5)
  splash:evaljs(js)
  assert(splash:set_viewport_full())
  assert(splash:wait(args.wait))
  return splash:html()
end
'''


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    base_url = 'https://www.jd.com/'

    def start_requests(self):
            for page in range(1, self.settings.get('MAX_PAGE')):
                yield SplashRequest(url=self.base_url, callback=self.parse,endpoint='execute', args={
                    'lua_source': lua, 'page': page, 'wait': 10,'keywords':self.settings.get('KEYWORDS')
                })
    def parse(self, response):
        goods_list = response.xpath("//div[@class='gl-i-wrap']")
        for good in goods_list:
            price = good.xpath("./div[@class='p-price']/strong/i/text()").get()
            name = good.xpath("./div[contains(@class,'p-name')]/a/i/text()").get()
            shop = good.xpath("./div[@class='p-shop']/span/a/text()").get()
            item={
                'name':name,
                'price':price,
                'shop':shop
            }
            print(item)
            return item
