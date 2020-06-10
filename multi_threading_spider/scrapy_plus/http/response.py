# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

from lxml import etree

class Response():

    def __init__(self, url, status_code, headers, body):

        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def xpath(self, xpath_str):
        html = etree.HTML(self.body)
        return html.xpath(xpath_str)