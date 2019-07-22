# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.http import HtmlResponse



class GuaziMiddleware(object):
    def process_request(self,request,spider):
        url=request.url
        spider.chrome.get(url)
        html=spider.chrome.page_source
        return HtmlResponse(url=url,body=html,request=request,encoding='utf-8')
