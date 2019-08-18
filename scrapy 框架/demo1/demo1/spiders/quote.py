# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['goodreads.com/quotes']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response):
        quotes = response.css('.quoteDetails')
        for quote in quotes:
            try:
                author = quote.css('.leftAlignedImage img').attrib['alt']
            except:
                author = ''
            try:
                avatar = quote.css('.leftAlignedImage img').attrib['src']
            except:
                avatar = ''
            content = quote.css('.quoteText::text').get()
            tags = quote.css('.quoteFooter .smallText a::text').getall()
            likes = quote.css('.quoteFooter .right .smallText::text').get()

            info = {
                'author': author,
                'avatar': avatar,
                'content': content,
                'tags': tags,
                'likes': likes
            }
            yield info
