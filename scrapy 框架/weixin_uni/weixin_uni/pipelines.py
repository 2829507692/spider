# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter


class WeixinUniPipeline(object):
    def open_spider(self,spider):
        self.fp=open('wxapp.json','wb')
        self.expoter=JsonLinesItemExporter(
            self.fp,
            ensure_ascii=False,
        )

    def process_item(self, item, spider):
        self.expoter.export_item(item)
        return item

    def close_spider(self,spide):
        self.fp.close()
