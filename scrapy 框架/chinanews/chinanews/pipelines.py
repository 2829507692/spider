# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from .data_filter.memory_filter import MemoryFilter

filters=MemoryFilter()

class ChinanewsPipeline(object):
    def process_item(self, item, spider):
        if filters.is_exist(json.dumps(dict(item))):
            raise DropItem('数据已经存在！！')
        else:
            filters.save(json.dumps(dict(item)))
        print(item)
