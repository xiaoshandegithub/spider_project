# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from suanfatujie.items import SuanfatujieItem

class SuanfaSpiderSpider(RedisSpider):
    name = 'suanfa_spider'
    allowed_domains = ['www.cxyxiaowu.com/']
    redis_key = 'suanfa'
    # start_urls = ['http://xxx/']

    def start_requests(self):
        cookie_str = 'PHPSESSID=9gjffvcc82tvlla3ditlbar5bc; Hm_lvt_52c0281453695a300fbc7c3cbdeb4551=1591661182; Hm_lpvt_52c0281453695a300fbc7c3cbdeb4551=1591661222'
        # 字典生成式 生成 cookie字段
        cookies_dict = {cookie_line.split('=')[0]: cookie_line.split('=')[1] for cookie_line in cookie_str.split('; ')}
        headers = {}
        headers['referer'] = "https://www.cxyxiaowu.com/suanfa-2/suanfa"
        # headers[':path'] = "/suanfa-2/suanfa/page/2"
        # headers[':authority'] = "www.cxyxiaowu.com"
        # headers[':method'] = "GET"
        # headers[':scheme'] = "scheme"
        headers['accept'] = "*/*"
        headers['x-requested-with'] = "XMLHttpRequest"
        headers['user-agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, cookies=cookies_dict, headers=headers)

    def parse(self, response):
        print('*' * 100)
        self.parse_comtent(response)
        base_url = "https://www.cxyxiaowu.com/suanfa-2/suanfa/page/"
        for i in range(2, 100):
            url = base_url + str(i)
            yield Request(url, callback=self.parse_comtent)

    def parse_comtent(self, response):
        print('*' * 100)
        item = SuanfatujieItem()
        div_lines = response.xpath('//*[@class="row posts-wrapper"]/div')
        for line in div_lines:
            item['title'] = line.xpath('.//article/div[2]/header/h2/a/text()')
            item['image_src'] = line.xpath('.//article/div[1]/div[1]/a/img/@data-src')
            print(item)
            yield item



