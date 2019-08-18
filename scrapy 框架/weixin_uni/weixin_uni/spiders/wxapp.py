# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pg']//a"), follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-1\.html'),callback='parse_detail',follow=False)
    )

    def parse_detail(self, response):
        title=response.css('.ph::text').get()
        date=response.xpath('//span[@class="time"]/text()').get()
        blockquote=response.css('.blockquote p::text').get()
        item = {
            'title':title,
            'date':date,
            'blockquote':blockquote
        }
        return item
