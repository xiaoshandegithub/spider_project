# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-22 下午6:18 GMT+8

# 先导入框架自己的默认配置
from scrapy_plus.conf.default_settings import *
# 此时 DEFAULT_LOG_FILENAME = 'log.log'


# 根据 从哪里执行就从哪里导入的 原则
# 运行位置在项目路径下，项目路径下有settings.py
# 下面导入的这个settings就是项目中的settings.py
from settings import *
# 此时 DEFAULT_LOG_FILENAME = '日志.log'
# 于是 项目中的配置的变量就把 框架的默认配置的变量 覆盖了！
