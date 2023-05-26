# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm
# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : compare_ofd.py
# @software: pycharm

import requests
# import json
import os
from fake_useragent import UserAgent
from logger import Logger
from configparser import ConfigParser
import csv
import time
import pywintypes

logger = Logger(logger='Compare_Test').getlog()


class Compare(object):
    """无GUI对比工具主程序"""

    def __init__(self):
        ua = UserAgent(path='./config/agent.json')
        self.headers = {'User-Agent': '{}'.format(ua.random)}
        self.url = "http://172.16.14.104:4018/compare_file/"
        self.old_path = input("请输入基准文件夹路径：")
        self.new_path = input("请输入新文件夹路径：")
        # 读取api5接口地址
        conf = ConfigParser()
        conf.read('./config/config.ini', encoding='utf-8')
        url = conf.get('api5_url', 'compare_url')
        logger.info("api5接口地址：{}".format(url))

    # def compare_ofds(self,old_path,new_path):
    #     benchmark_list = self.get_filepath(old_path)
    #     new_filelist = self.get_filepath(new_path)
    #     print(str(benchmark_list)+"\n"+str(new_filelist))
    #     return benchmark_list,new_filelist

    def get_filepath(self, path):
        """获取文件夹下的所有文件名称，返回列表"""
        file_list = os.listdir(path)
        # print(type(file_list))
        return file_list

    def post_requests(self, path1, path2):
        file_data = {"actual_file": open(path1, 'rb'),
                     "base_file": open(path2, 'rb')}
        try:
            rs = requests.post(url=self.url, files=file_data, headers=self.headers)
        except Exception as e:
            logger.warning(e.args)
        # rs = requests.post(url=url,files=files,headers=headers)
        # print(json.loads(rs.text))
        # print(rs.status_code)
        # print(json.loads(rs.text))
        return rs.status_code, rs.text

    def get_requests(self, url):
        res = requests.get(url=url)
        logger.info(res.status_code)
        return res.status_code

    def write_csv(self, file_name, content):
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["基准文件夹", "新文件夹", "对比结果", "详细信息"])
            writer.writerows(content)

    def main(self):
        res_get_code = self.get_requests('http://172.16.14.104:4018/docs#')
        if res_get_code == 200:
            logger.info("地址访问正常")
            file_list1 = self.get_filepath(self.old_path)
            file_list_2 = self.get_filepath(self.new_path)
            file_name = "./compare_result/result_{}.csv".format(str(time.time()).split('.')[0])
            res_list = []
            if set(file_list1) == set(file_list_2):
                logger.info("两个文件夹内的文件名称一致，开始比对")
                for list in file_list1:
                    path1 = self.old_path + "\\" + list
                    path1 = str(path1).replace("\\", "\\\\")
                    logger.info(path1)
                    path2 = self.new_path + "\\" + list
                    path2 = str(path2).replace("\\", "\\\\")
                    logger.info(path2)
                    code, message = self.post_requests(path1, path2)
                    # logger.info(type(code))
                    if code == 200:
                        res_list.append([path1,path2,"一致"])
                        # logger.info(file_name)
                        logger.info(path1 + "->" + path2 + "内容一致")
                    elif code== 500:
                        res_list.append([path1, path2, "对比结果异常，返回值：{}".format(code)])
                        logger.error("对比错误，请检查文件: {}<->{}".format(path1,path2))
                        continue
                    else:
                        res_list.append([path1, path2, "内容不一致，返回值：{}".format(code), message])
                        logger.warning(path1 + "->" + path2 + "内容不一致")
                    # time.sleep(5)
            else:
                logger.error("两个文件夹内的文件内容不一致，请检查")
        else:
            logger.error("地址访问异常，请检查！")
        self.write_csv(file_name=file_name,  content=res_list)
        logger.info("对比完成")


if __name__ == '__main__':
    start = Compare()
    start.main()
    # start.write_csv()
