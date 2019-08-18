# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import InfoItem,CententItem

class ZwduSpider(CrawlSpider):
    name = 'zwdu'
    allowed_domains = ['zwdu.com']
    start_urls = ['http://zwdu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.zwdu.com/book/\d{4,5}/$'), callback='parse_items', follow=True,),
        Rule(LinkExtractor(allow='https://www.zwdu.com/\w+/$'),callback='parse_items',follow=True),
    )

    def parse_items(self, response):
        name=response.xpath('//h1/text()').get()
        author=response.css('#info > p:nth-child(2)::text').get()
        category=response.css(".con_top > a:nth-child(2)::text").get()
        abstract=response.css("#intro p:first-child::text").get()
        url=response.xpath("//dd[1]//a[1]/@href").get()
        #print(name,author,category,start_url)
        item=InfoItem()
        item['name']=name
        item['author']=author
        item['category']=category
        item['abstract']=abstract

        if url is not None:
            start_url=self.start_urls[0]+str(url)
            yield scrapy.Request(url=start_url,callback=self.parser_per_page,meta={'name':name})

            yield item

    def parser_per_page(self,response):
        title=response.xpath('//h1/text()').get()
        content=response.xpath('//div[@id="content"]/text()').getall()
        next=response.xpath("//div[@class='bottem2']//a[3]/@href").get()
        name=response.request.meta.get('name',None)
        next_url=self.start_urls[0]+str(next)

        yield scrapy.Request(next_url,callback=self.parser_per_page,meta={'name':name})

        item=CententItem()
        item['name']=name
        item['title']=title
        item['content']=content

        yield item