# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

import datetime
import importlib
from multiprocessing.dummy import Pool
from scrapy_plus.core.spider import Spider
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.http.request import Request

from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware

from scrapy_plus.utils.log import logger

from scrapy_plus.conf.settings import SPIDERS, PIPELINES, SPIDER_MIDDLEWARES, \
    DOWNLOADER_MIDDLEWARES, MAX_REQUEST_NUMS

class Engine():

    def __init__(self):
        self.spiders = self._auto_import_ret(path=SPIDERS, isspider=True)
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipelines = self._auto_import_ret(path=PIPELINES)

        self.spider_mids = self._auto_import_ret(path=SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_ret(path=DOWNLOADER_MIDDLEWARES)

        self.total_request_nums = 0
        self.total_response_nums = 0

        self.pool = Pool(MAX_REQUEST_NUMS)
        self.is_running = True

    def _auto_import_ret(self, path=[], isspider=False):
        """利用动态导包的方式，自动根据配置获取爬虫字典或管道、中间件列表"""
        ret = {} if isspider else []
        for p in path: # 'spiders.baidu.BaiduSpider'
            py_name_str = p.rsplit('.', 1)[0] # 'spiders.baidu'
            cls_name_str = p.rsplit('.', 1)[1] # 'BaiduSpider'
            # 利用importlib.import_module函数来根据执行位置.模块名字符串来获取模块对象
            py_obj = importlib.import_module(py_name_str)
            cls = getattr(py_obj, cls_name_str) #此时返回的是没有实例化的类对象！
            if isspider:
                ret[cls.name] = cls()
            else:
                ret.append(cls())
        return ret

    def start(self):
        # 入口函数
        start_time = datetime.datetime.now()
        logger.info('开始的时间：{}'.format(start_time))
        self._start_engine()
        end_time = datetime.datetime.now()
        logger.info('结束的时间：{}'.format(end_time))
        logger.info('耗时：{}'.format(end_time-start_time))
        logger.info('总请求数：{}'.format(self.total_request_nums))
        logger.info('总响应数：{}'.format(self.total_response_nums))
        logger.info('重复的请求数：{}'.format(self.scheduler.repeat_request_nums))

    def _start_requests(self):
        """把爬虫的所有起始url全部构造成request，放入队列"""
        # 1. 爬虫模块发出初始请求
        for spider_name,spider in self.spiders.items():
            for start_request in spider.start_requests():
                # 给request添加爬虫名的属性
                start_request.spider_name = spider_name
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request, spider)
                # 2. 把初始请求添加给调度器
                self.scheduler.add_request(start_request)
                # 总请求数 + 1
                self.total_request_nums += 1

    def execute_request_response_item(self):
        """把队列中取出的一个request进行处理，直到不再需要该request"""
        # 3. 从调度器获取请求对象
        request = self.scheduler.get_request()
        if request is None:
            return # 此时请求队列被取空
        # 通过request携带的spider_name来按键取出爬虫类对象
        spider = self.spiders[request.spider_name]

        # 利用下载器中间件预处理请求对象
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)
        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)
        # 传递meta!!!
        response.meta = request.meta
        # 利用下载器中间件预处理响应对象
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response, spider)
        # 利用爬虫中间件预处理响应对象
        for spider_mid in self.spider_mids:
            response = spider_mid.process_response(response, spider)

        # request.parse == 解析函数名字符串
        # 函数 = getattr(类对象, 类的函数名字符串)
        # 获取request在构造时指定的解析函数
        parse_func = getattr(spider, request.parse)

        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        results = parse_func(response)

        for result in results:
            # 6. 判断结果对象
            if isinstance(result, Request):
                # 给request添加爬虫名的属性
                result.spider_name = request.spider_name
                # result.spider_name = spider.name # 结果同上一行
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_request(result, spider)
                # 6.1 如果是请求对象，那么就再交给调度器
                self.scheduler.add_request(result)
                # 总请求数 + 1
                self.total_request_nums += 1
            else:
                # 6.2 否则，就交给管道处理
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)

        # 总响应数 + 1
        self.total_response_nums += 1

    def _callback(self, temp):
        if self.is_running:
            self.pool.apply_async(func=self.execute_request_response_item,
                                  callback=self._callback)


    def _start_engine(self):
        # 调用其他组件的属性或函数来组织运行的逻辑

        self._start_requests()

        for i in range(MAX_REQUEST_NUMS): # 通过配置来控制并发规模
            self.pool.apply_async(func=self.execute_request_response_item,
                                  callback=self._callback)

        while True:
            # 程序退出的条件：总响应数 + 重复请求数 == 总请求数
            if self.total_response_nums + self.scheduler.repeat_request_nums == self.total_request_nums:
                self.is_running = False
                break


