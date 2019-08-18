# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class ChinanewsItem(scrapy.Item):
    url=scrapy.Field(
        output_processor=TakeFirst()
    )
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=MapCompose(remove_tags,),
        output_processor=TakeFirst(),
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_tags,),
        output_processor=TakeFirst(),
    )