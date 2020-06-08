# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class WendaDemo2Spider(RedisCrawlSpider):
    name = 'wenda_demo2'
    allowed_domains = ['www.guokr.com']
    # start_urls = ['https://www.guokr.com/ask/pending/']
    redis_key = 'wenda_02'

    rules = (
        Rule(LinkExtractor(allow=r'/ask/pending/\?page=\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'www\.guokr\.com/question/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['content'] = response.xpath("//div[@id='questionDesc']/p/text()").extract_first()
        return item
