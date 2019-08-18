#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-08-09 17:32:40
# Project: qunaer

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        "validate_cert":False,
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://travel.qunar.com/?from=header', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('h2 > a').items():
            self.crawl(each.attr.href, callback=self.detail_page,fetch_type='js')
        next=response.doc('.next')
        self.crawl(next.attr.href,callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('#booktitle').text(),
            "data":response.doc('.when .data').text(),
            "day":response.doc('.howlong  .data').text(),
            "who" :response.doc('.who .data').text(),
            "text":response.doc('#b_panel_schedule').text(),
            "img":response.doc('.cover_img').attr.src
        }