# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午5:01 GMT+8

class DownloaderMiddleware(object):
    '''下载器中间件基类'''

    def process_request(self, request):
        '''预处理请求对象'''
        print("这是下载器中间件：process_request方法")
        return request

    def process_response(self, response):
        '''预处理响应对象'''
        print("这是下载器中间件：process_response方法")
        return response