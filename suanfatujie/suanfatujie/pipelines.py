# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SuanfatujiePipeline:

    def open_spider(self, spiser):
        self.f = open('suanfa.txt', 'w')

    def process_item(self, item, spider):
        write_str = item['title'] + item['image_src'] + '\r\n'
        self.f.write(write_str)
        return item

    def close_spider(self, spider):
        self.f.close()