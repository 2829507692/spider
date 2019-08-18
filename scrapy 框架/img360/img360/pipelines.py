# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class Img360Pipeline(object):
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(spider.settings.get('MONGO_URI'))
        self.db=self.client[spider.settings.get('MONGO_DATABASE')]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db.img360.insert_one(item)
        return item

import pymysql
class MysqlPipeline(object):
    def open_spider(self,spider):
        self.conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='img360')
        self.cur=self.conn.cursor()

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        keys=','.join(item.keys())
        values=','.join(['%s']*len(item))
        sql='insert into img360 (%s) values (%s)'%(keys,values)
        self.cur.execute(sql,tuple(item.values()))
        self.conn.commit()
        return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
    #返回文件名
    def file_path(self, request, response=None, info=None):
        url=request.url
        image_name=url.split('/')[-1]
        return image_name
    #生成请求
    def get_media_requests(self, item, info):
        url=item['qhimg_url']
        yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item