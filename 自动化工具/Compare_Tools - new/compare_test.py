# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm

import json

import requests
# import json
import os
from fake_useragent import UserAgent
from logger import Logger
from configparser import ConfigParser
import csv
import time
from pathlib import Path

logger = Logger(logger='Compare_Test').getlog()

class Compare(object):
    """无GUI对比工具主程序"""

    def __init__(self):
        ua = UserAgent()
        # ua.update(use_external_data=True)
        ua.load("./config/agent.json")
        # 生成随机的User-Agent信息
        self.headers = {'User-Agent': '{}'.format(ua.random)}
        self.old_path = input("请输入基准文件夹路径：")
        self.new_path = input("请输入新文件夹路径：")
        # 读取api5接口地址
        conf = ConfigParser()
        conf.read('./config/config.ini', encoding='utf-8')
        self.url = conf.get('api5_url', 'compare_url')
        logger.info("api5接口地址：{}".format(self.url+"compare_file/"))


    def get_filepath(self, path):
        """获取文件夹下的所有文件名称，返回列表"""
        file_list = os.listdir(path)
        # print(type(file_list))
        return file_list

    def post_requests(self,url, path1, path2):
        file_data = {"actual_file": open(path1, 'rb').read(),
                     "base_file": open(path2, 'rb').read(),
                     # "export_result": False,
                     # "sim": "0.9999",
                     # "p_page_render_pic": True,
                     # "p_page_annots": True,
                     # "p_metadatas": True,
                     # "p_attachments": True,
                     # "p_outlines": True,
                     # "p_bookmarks": True,
                     # "p_customTags": True,
                     # "p_signatures": True,
                     # "p_page_info": True,
                     # "p_page_text": True,
                     # "p_page_layer_count": True,
                     # "p_permissions": True,
                     # "p_fonts": True,
                     # "p_docActions": True,
                     # "p_page_actions": True,
                     # "p_page_objects": True,
                     # "kernel_size": 10,
                     }
        try:
            rs = requests.post(url=url, files=file_data, headers=self.headers)
        except Exception as e:
            logger.warning(e.args)
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
        res_get_code = self.get_requests(self.url+'docs#/')
        if res_get_code == 200:
            logger.info("地址访问正常")
            file_list1 = self.get_filepath(self.old_path)
            file_list_2 = self.get_filepath(self.new_path)
            file_name = "./compare_result/result_{}.csv".format(str(time.time()).split('.')[0])
            res_list = []
            if set(file_list1) == set(file_list_2):
                logger.info("两个文件夹内的文件名称一致，开始比对")
                scale = len(file_list1)
                i = 1
                starttime = time.perf_counter()
                for list in file_list1:
                    a = '*' * i
                    b = '~' * (scale - i)
                    c = (i / scale) * 100
                    dur = time.perf_counter() - starttime

                    path1 = Path(self.old_path + "\\" + list)
                    # logger.info(path1)
                    path2 = Path(self.new_path + "\\" + list)
                    # logger.info(path2)
                    code, message = self.post_requests(self.url+"compare_file/",path1, path2)
                    # logger.info(type(code))
                    if code == 200:
                        res_list.append([path1,path2,"一致"])
                        # logger.info(file_name)
                        logger.info(str(path1) + "->" + str(path2) + "内容一致")
                    elif code== 500:
                        res_list.append([path1, path2, "对比结果异常，返回值：{}".format(code)])
                        logger.warning("对比错误,返回值：{}，请检查文件: {}<->{}".format(code,path1,path2))
                        # continue
                    else:
                        res_list.append([path1, path2, "内容不一致，返回值：{}".format(code), message])
                        logger.warning(str(path1) + "->" + str(path2) + "内容不一致,返回值：{},返回信息：{}".format(code,json.loads(message)))
                    print("\r{:^3.0f}%[{}->{}] <{}> {:.2f}s".format(c, a, b,list, dur), end="")
                    # print(i)
                    i = i+1
            else:
                logger.error("两个文件夹内的文件内容不一致，请检查")
        else:
            logger.error("地址访问异常，请检查！")
        self.write_csv(file_name=file_name,  content=res_list)
        print("\n结果文件保存路径：{}".format(file_name))
        logger.info("对比完成")


if __name__ == '__main__':
    start = Compare()
    start.main()
    # start.write_csv()
