# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

import six
import hashlib
from queue import Queue
from w3lib.url import canonicalize_url

from scrapy_plus.utils.log import logger


class Scheduler():

    def __init__(self):
        self.q = Queue()
        self.fp_set = set()
        self.repeat_request_nums = 0

    def add_request(self, request):
        # 把request放入队列
        if self._filter_request(request): # 指纹不在集合中，返回True，指纹入集合请求入队
            self.q.put(request)

    def get_request(self):
        # 取出一个request并返回
        try:
            request = self.q.get(False) # get_nowait()
        except:
            request = None
        return request

    def _filter_request(self, request):
        # 过滤去重，暂不实现
        fp = self._gen_fp(request)
        if fp not in self.fp_set: # 判断如果指纹不在集合中
            self.fp_set.add(fp) # 于是，就把指纹放入集合中
            return True # 返回True 请求可以入队
        logger.info('发现重复的请求：<{}>'.format(request.url))
        self.repeat_request_nums += 1
        return False # 请求重复了，返回False

    def _gen_fp(self, request):
        # 根据request生成fp并返回
        url = canonicalize_url(request.url)
        method = request.method.upper()
        data = sorted(request.data.items(), key=lambda x:x[0])
        # [(a,2), (b,1)]
        # x表示被排序的对象每次迭代返回的值; x[0]就表示按照每次迭代的对象的下标为0的那个值进行排序
        data_str = str(data)

        s1 = hashlib.sha1()
        s1.update(self._to_bytes(url))
        s1.update(self._to_bytes(method))
        s1.update(self._to_bytes(data_str))
        fp = s1.hexdigest()

        return fp

    def _to_bytes(self, string):
        # 不管进来的参数是bytes还是str，最终返回的都必须是bytes
        if six.PY3:
            if isinstance(string, str):
                return string.encode()
            else:
                return string
        # 字符串 在Py2 和 Py3中 在str和bytes上 正好相反
        elif six.PY2:
            if isinstance(string, str):
                return string
            else:
                return string.encode()