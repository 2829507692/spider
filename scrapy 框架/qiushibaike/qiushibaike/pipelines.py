# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import json
import re

class QiushibaikePipeline(object):
    def __init__(self):
        self.f=open('./糗事百科.json','wb')
        self.exportor=JsonItemExporter(self.f,ensure_ascii=False)

    def open_spider(self,spider):
        print('start')
        self.exportor.start_exporting()

    def process_item(self, item, spider):
        print(item)
        item=self.filter(item)
        self.exportor.export_item(item)

    def close_spider(self,spider):
        print('end')
        self.exportor.finish_exporting()
        self.f.close()

    def filter(self,item):
        l={}
        for i in item:
            value=re.sub('\n','',item[i])
            key=re.sub('\n','',i)
            l.setdefault(key,value)
        return l

