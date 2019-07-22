# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class Sun0769Pipeline(object):
    def process_item(self, item, spider):
        item['content']=self.conten_parser(item['content'])
        print(item)
        return item
    def conten_parser(self,content):
        content=re.sub('\xa0|\s','',content)
        return content

