# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo
import scrapy

class Demo1Pipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(spider.settings.get('MONGO_URI'))
        self.db = self.client[spider.settings.get('MONGO_DATABASE')]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(item)
        if len(item['author'])>=10:
            item['author']=item['author'][:10]

        item['content']=re.search(r'\w.*?\.',item['content']).group()

        self.db.quote.insert_one(item)
        return item
