# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .items import CententItem, InfoItem
import re

class BasePipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

class ByzwwPipeline(BasePipeline):
    def process_item(self, item, spider):
        if isinstance(item, InfoItem):
            ab=item['abstract']
            if ab :
                abstract = re.sub(r'[\s|\n]+', '', ab)
                item['abstract'] = abstract
                self.db[item['name']].insert_one(dict(item))
                print(item)
        return item

class ContentPipeline(BasePipeline):
    def process_item(self, item, spider):
        if isinstance(item,CententItem):
            ct=item['content']
            sum=''
            for i in ct:
                i=re.sub(r'[\s|\n]+', '',i)
                sum+=i
            content =sum
            item['content'] = str(content)
            s=dict(item)
            name=s.pop('name')
            print(name ,s)
            self.db[name].insert_one(s)
        return item