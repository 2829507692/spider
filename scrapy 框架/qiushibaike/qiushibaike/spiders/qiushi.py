# -*- coding: utf-8 -*-
import scrapy
import os

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        list_item=response.xpath("//div[@class='col1']/div")
        for item in list_item:
            name=item.xpath('./div[contains(@class,"author")]/a[2]/h2/text()').get()
            cottent=item.xpath('./a/div/span/text()').get()
            dic={
                'name':name,
                'contents':cottent

            }
            yield dic

        # next=response.xpath("//span[@class='next']").get()
        # if next:
        #     url=response.xpath("//div[@id='content-left']//li[8]//a[1]/@href").get()
        #     yield scrapy.Request(os.path.join(self.start_urls[0],url),callback=self.parse)