# -*- coding: utf-8 -*-
import scrapy
from  sun0769.items import Sun0769Item

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/reply.shtml']

    def parse(self, response):
        tr_list=response.xpath("//div[contains(@class,'clearfix')]/table[2]//tr")
        for tr in tr_list:
            item=Sun0769Item()
            item['title']=tr.xpath('./td[3]/a/@title').get()
            item['page_info']=tr.xpath('./td[@class="txt18"]/a/@href').get()
            item['date']=tr.xpath('./td[6]/text()').get()
            # print(item)
            yield scrapy.Request(url=item['page_info'],callback=self.page_parser,meta={'item':item})

        next_page=response.xpath("//a[text()='>']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)

    def page_parser(self,response):
        item=response.meta['item']
        item['content']=response.xpath("string(//td[@class='txt16_3'])").get()
        item['img'] = response.xpath("//div[@class='textpic']//img/@src").get()
        if item['img']:
            item['img']= 'http://wz.sun0769.com/'+item['img']
        yield item
