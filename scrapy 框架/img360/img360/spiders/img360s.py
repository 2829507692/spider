# -*- coding: utf-8 -*-
import scrapy
import json

# start_urls = ['http://images.so.com/']

class Img360sSpider(scrapy.Spider):
    name = 'img'
    max_page=10

    allowed_domains = ['images.so.com']

    def start_requests(self):
        for i in range(0,self.max_page):
            url='http://images.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'.format(i*30)
            print(url)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        file=response.text
        dics=json.loads(file).get('list')
        for line in dics:
            info={
                'id':line.get('id'),
                'title':line.get('title'),
                'imgsurl':line.get('purl'),#图片合集地址
                'qhimg_url':line.get('qhimg_url'),#首张图片地址
                'qhimg_thumb':line.get('qhimg_thumb')#缩略图
            }
            yield info

