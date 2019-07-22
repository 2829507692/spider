# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://xa.lianjia.com/ershoufang/pg{}/'.format(i) for i in range(1,11)]

    def parse(self, response):
        base_url=response.xpath('//div[@class="title"]/a/@href').getall()
        for i in base_url:
            yield scrapy.Request(url=i,callback=self.page_parser)

    def page_parser(self,response):
        price=response.xpath('//span[@class="total"]/text()').get()
        unit=response.xpath('//span[@class="unit"]//span/text()').get()
        unit_price=response.xpath('string(//span[@class="unitPriceValue"])').get()
        community=response.xpath('//a[@class="info no_resblock_a"]/text()').get()
        area=response.xpath('string(//div[@class="areaName"]//span[2])').get()
        house_type=response.xpath("//div[@class='base']//div[@class='content']/ul/li[1]/text()").get()
        house_floor=response.xpath("//div[@class='base']//div[@class='content']/ul/li[2]/text()").get()
        house_area=response.xpath("//div[@class='base']//div[@class='content']/ul/li[3]/text()").get()
        house_year=response.xpath("//div[@class='base']//div[@class='content']/ul/li[last()]/text()").get()
        yield {
            'price':price,
            'unit':unit,
            'unit_price':unit_price,
            'community':community,
            'area':area,
            'house_type':house_type,
            'house_floor':house_floor,
            'house_area':house_area,
            'house_year':house_year
        }
