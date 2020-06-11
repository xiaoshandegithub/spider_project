# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DoubanPipeline:
    def open_spider(self, spider):
       self.f = open("xxx.txt", 'w', encoding='utf8')

    def process_item(self, item, spider):
        self.f.write(json.dumps(item) + '\r\n')
        return item

    def close_spider(self, spider):
        self.f.close()


