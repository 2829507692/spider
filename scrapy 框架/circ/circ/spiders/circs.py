# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CircsSpider(CrawlSpider):
    name = 'circs'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab7324/module25157/page1.htm']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//span[@id='lan1']/a"), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='Normal page_custom']"),follow=True)
    )

    def parse_item(self, response):
        item={}
        item['title']=(re.search(r'<!--TitleStart-->(.*?)<!--TitleEnd-->',response.text)).group(1)
        data=re.search(r'20\d{2}年\d{1,2}月\d{1,2}日',response.text)
        if data is not None:
            item['data']=data.group(0)
        print(item)
