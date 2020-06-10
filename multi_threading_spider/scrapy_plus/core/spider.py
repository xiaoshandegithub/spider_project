# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

from scrapy_plus.http.request import Request
from scrapy_plus.item import Item


class Spider():

    name = '爬虫名'

    start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)

    def parse(self, response):
        return Item(response)