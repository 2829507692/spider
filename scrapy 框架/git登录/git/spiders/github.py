# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response,
        formdata={'login':'2829507692@qq.com',
                  'password':'f7345968hejie'
        },callback=self.after_parser)
    def after_parser(self,response):
        print(response.text)