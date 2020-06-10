# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午6:20 GMT+8

DEFAULT_LOG_FILENAME = '日志.log'    # 更改默认配置

# 启用的爬虫类
SPIDERS = [
    'spiders.baidu.BaiduSpider',
    'spiders.douban.DoubanSpider'
]

# 启用的管道类
PIPELINES = [
    'pipelines.BaiduPipeline',
    'pipelines.DoubanPipeline'
]

# 启用的爬虫中间件类
SPIDER_MIDDLEWARES = []

# 启用的下载器中间件类
DOWNLOADER_MIDDLEWARES = []

MAX_REQUEST_NUMS = 8