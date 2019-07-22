# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from selenium import webdriver

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/xa/buy/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(GuaziSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.chrome = webdriver.Chrome()
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        print(spider.name)
        spider.chrome.quit()

    def parse(self, response):
        print(response.text)
