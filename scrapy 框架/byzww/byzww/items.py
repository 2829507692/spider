# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoItem(scrapy.Item):
    name =scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    abstract=scrapy.Field()


class CententItem(scrapy.Item):
    name=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()