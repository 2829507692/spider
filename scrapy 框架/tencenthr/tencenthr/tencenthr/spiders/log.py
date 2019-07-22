# -*- coding: utf-8 -*-
import scrapy
import logging
loger=logging.getLogger(__name__)

class LogSpider(scrapy.Spider):
    name = 'log'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        for i in range(10):
            # logging.warning(i*'*') #直接以警告及输出到控制台
            loger.warning('*'*i*i)#显示来源输出