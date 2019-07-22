# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import Demo01Item
class Demo01Pipeline(object):
    def open_spider(self,spider):
        self.client=pymongo.MongoClient()
        self.collection=self.client['tencent']['hr']

    def process_item(self, item, spider):
        if isinstance(item,Demo01Item):
            self.collection.insert(item)

    def close_spider(self,spider):
        self.client.close()
