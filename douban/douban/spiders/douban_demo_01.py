# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request


class DoubanDemo01Spider(scrapy.Spider):
    name = 'douban_demo_01'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20']

    def parse(self, response):
        usr_first = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start='
        limit_str = "&limit=20"
        # print(response)
        response_str = json.loads(response.body_as_unicode())
        # print(response_str)
        for line_json_dict in response_str:
            item = {}
            item['title'] = line_json_dict['title']
            item['url'] = line_json_dict['url']
            yield item
        if response != None:
            for url_num in range(0, 100000, 20):
                url = usr_first + str(url_num) + limit_str
                yield Request(url, callback=self.parse)
