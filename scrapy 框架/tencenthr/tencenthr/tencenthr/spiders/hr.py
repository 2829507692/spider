# -*- coding: utf-8 -*-
import scrapy
import js2py
from jsonpath import jsonpath
import json
s="(new Date).getTime()"
data=js2py.eval_js(s)
class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={0}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={1}&pageSize=10&language=zh-cn&area=cn'.format(data,i) for i in range(1,11)]

    def parse(self, response):
        res=json.loads(response.text,encoding='utf-8')
        datas = jsonpath(res,'$.Data.Posts.*')
        for data in datas:
            yield data
    #         yield scrapy.Request(callback=self.paser1,meta={'data':data})
    # def paser1(self):
    #     pass
