# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午3:58 GMT+8

import requests
from scrapy_plus.http.response import Response


class Downloader():

    def get_response(self, request):
        # 发送请求获取响应
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers,
                                 data=request.data)
        else:
            raise Exception('不支持的发送请求的方式：{}'.format(request.method))

        return Response(url=resp.url, status_code=resp.status_code,
                        headers=resp.headers, body=resp.content)