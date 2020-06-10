# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

class Request():

    def __init__(self, url, method='GET',
                 headers=None, data={},
                 parse='parse', meta={}):

        self.url = url
        self.method = method
        self.headers = headers
        self.data = data

        self.parse = parse
        self.meta = meta