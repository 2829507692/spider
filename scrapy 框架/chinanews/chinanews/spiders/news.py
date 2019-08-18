# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ChinanewsItem
from scrapy.loader import ItemLoader

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.china.com']
    start_urls = ['https://news.china.com/domestic/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+index\.html'), follow=True,),
        Rule(LinkExtractor(allow=r'https://news.china.com/international/\d+/\d+/\d+\.html'),callback='parse_detail', follow=False,)
    )

    def parse_detail(self, response):
        item = ItemLoader(item=ChinanewsItem(),response=response)
        item.add_css('title','#chan_newsTitle::text')
        item.add_css('time','.time::text')
        item.add_css('author','.source>a::text')
        item.add_value('url', response.url)

        return item.load_item()
