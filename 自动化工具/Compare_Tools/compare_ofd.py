# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : compare_ofd.py
# @software: pycharm

import requests
import json
import os
import sys
from fake_useragent import UserAgent
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_test import *

class Compare(object):
    def compare_ofds(self,old_path,new_path):
        benchmark_list = self.get_filepath(old_path)
        new_filelist = self.get_filepath(new_path)
        # print(benchmark_list+"\n"+new_filelist)
        return benchmark_list,new_filelist


    def get_filepath(self,path):
        """获取文件夹下的所有文件名称，返回列表"""
        file_list = os.listdir(path)
        return file_list

    def test(self,url,headers,files):
        rs = requests.post(url=url,files=files,headers=headers)
        # rs = requests.post(url=url,files=files,headers=headers)
        # print(json.loads(rs.text))
        return rs.status_code,json.loads(rs.text)


if __name__=='__main__':
    ua = UserAgent(path='agent.json')
    url = "http://172.16.14.104:4018/compare_file/"
    headers = {'User-Agent': '{}'.format(ua.random)}
    files = {"actual_file": open("D:\\1.ofd", 'rb'),
               "base_file": open("D:\\URI.ofd", 'rb')}
    start = Compare()
    start.test(url=url,files=files,headers=headers)
