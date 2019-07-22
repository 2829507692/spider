# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class RoomPipeline(object):
    def open_spider(self,spider):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='room',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.connection.cursor()


    def process_item(self, item, spider):
        args=(
            item['price'],
            item['unit'],
            item['unit_price'],
            item['community'],
            item['area'],
            item['house_type'],
            item['house_floor'],
            item['house_area'],
            item['house_year'],
        )
        print(args)
        sql = "INSERT INTO `lianjia` (`price`, `unit`,`unit_price`,`community`,`area`,`house_type`,`house_floor`,`house_area`,`house_year`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,[i for i in item.values()])
        self.connection.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connection.close()
