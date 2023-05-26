# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2019/1/14 21:45
'''

import logging
import logging.handlers
import os.path
import time
from Multiprocesslog import MultiprocessHandler

# class Logger(object):
#
#     def __init__(self, logger):
#         '''
#                     指定保存日志的文件路径，日志级别，以及调用文件
#                     将日志存入到指定的文件中
#                 '''
#         log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
#         log_name = log_path + 'autotest' + '.log'
#         # 创建一个logger
#         self.logger = logging.getLogger(logger)
#         self.logger.setLevel(logging.DEBUG)
#
#         # 创建一个handler，用于写入日志文件
#         fh = TimedRotatingFileHandler(os.path.join(log_path, "autotest.log"), when="midnight", interval=1, backupCount=5)
#         # fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1048576, backupCount=10, encoding='utf-8')
#         fh.setLevel(logging.DEBUG)
#         # fh.suffix = "%Y-%m-%d_%H-%M-%S.log"
#
#         # 再创建一个handler，用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#
#         # 定义handler的输出格式
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # 给logger添加handler
#         self.logger.addHandler(fh)
#         self.logger.addHandler(ch)
#         fh.close()
#
#     def getlog(self):
#         return self.logger



class Logger(object):

    def __init__(self, logger):
        '''
                    指定保存日志的文件路径，日志级别，以及调用文件
                    将日志存入到指定的文件中
                '''
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_name = 'light_reader' + '.log'
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件.when-分割日志的时间间隔（S/每秒，M/每分钟，H/每小时，D/每天），backupcount-保留的log数量
        fh = MultiprocessHandler(filename=log_name, when='D' ,backupCount=7)
        # 设置日志的输出等级
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        fh.close()

    def getlog(self):
        return self.logger