# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-23 下午4:15 GMT+8

class TestDownloaderMiddleware1(object):

    def process_request(self, request, spider):
        '''处理请求头，添加默认的user-agent'''
        print("TestDownloaderMiddleware1: process_request")
        return request

    def process_response(self, response, spider):
        '''处理数据对象'''
        print("TestSDownloaderMiddleware1: process_response")
        return response


class TestDownloaderMiddleware2(object):

    def process_request(self, request, spider):
        '''处理请求头，添加默认的user-agent'''
        print("TestDownloaderMiddleware2: process_request")
        return request

    def process_response(self, response, spider):
        '''处理数据对象'''
        print("TestDownloaderMiddleware2: process_response")
        return response