# -- coding: utf-8 --
# @time :  2022/11/01
# @author : 马维畅
# @file : main_window.py
# @software: pycharm

import sys
from pathlib import Path

import compare_ofd
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from fake_useragent import UserAgent

from main_test import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.my_thread = MyThread()
        self.my_thread.my_str.connect(self.compare)
        self.cme = compare_ofd.Compare()
        ua = UserAgent(path='agent.json')
        self.headers = {'User-Agent': '{}'.format(ua.random)}
        self.url = self.lineEdit_3.text()
        # 设置按钮点击动作
        self.toolButton.clicked.connect(lambda: self.choose_file(self.lineEdit))
        self.toolButton_2.clicked.connect(lambda: self.choose_file(self.lineEdit_2))
        self.pushButton.clicked.connect(self.compare)

    def choose_file(self,edit_name):
        path = QFileDialog.getExistingDirectory(self,"请选择文件夹","D:/")
        edit_name.setText(path)
        self.textEdit.append("选择的文件夹为：{}\n".format(path))

    def compare(self,out_str):
        if out_str == "ok":
            print("处理完成")
        # compare_result1,compare_result2 = self.cme.compare_ofds(self.lineEdit.text(),self.lineEdit_2.text())
        # # new_list = self.cme.compare_ofd(self.lineEdit_2.text())
        # print(compare_result1)
        # if set(compare_result1)==set(compare_result2):
        #     self.textEdit.append("两个文件夹内的文件名称一致，开始比对"+"\n")
        #     i = 1
        #     for file_list in compare_result1:
        #         # path1 = self.lineEdit.text() +"/"+file_list
        #         path1 = Path(self.lineEdit.text() +"/"+file_list)
        #         path1 = str(path1).replace("\\", "\\\\")
        #         # path2 = self.lineEdit_2.text() +"/"+ file_list
        #         path2 = Path(self.lineEdit_2.text() + "/" + file_list)
        #         path2 = str(path2).replace("\\", "\\\\")
        #         self.textEdit.append("<font color=\"#0F0F0F\">旧文件路径：{}</font> ".format(str(path1)))
        #         # self.textEdit.append("旧文件路径：" + str(path1))
        #         self.textEdit.append("<font color=\"#0F0F0F\">新文件路径：{}</font> ".format(str(path2)))
        #         # self.textEdit.append("新文件路径：" + str(path2))
        #         # print(self.url,self.headers)
        #         # print("当前文件路径："+path1)
        #         file_data = {"actual_file":open(path1,'rb'),
        #               "base_file":open(path2,'rb')}
        #         result,response = self.cme.test(url=self.url,headers=self.headers,files=file_data)
        #         # print(result)
        #         if result == 200:
        #             self.textEdit.append("<font color=\"#00FF00\"> Status：{}，两文件内容相同 </font> ".format(str(result)))
        #         elif result == 417:
        #             self.textEdit.append("<font color=\"#EE2C2C\"> Status：{}-{}，两文件存在差异 </font> ".format(str(result),response))
        #         else:
        #             self.textEdit.append("<font color=\"#0000FF\"> Status：{}，其他错误 </font> ".format(str(result)))
        #         self.progressBar.setProperty("value",int((i / len(compare_result1)) * 100))
        #         i+=1
        # else:
        #     self.textEdit.append("文件内容不一致，请检查")
        # self.textEdit.append("文件对比完成")


class MyThread(QThread):
    my_str = pyqtSignal(str) # 创建任务信号

    def run(self):
        self.my_thread.start()
        compare_result1, compare_result2 = self.cme.compare_ofds(self.lineEdit.text(), self.lineEdit_2.text())
        # new_list = self.cme.compare_ofd(self.lineEdit_2.text())
        print(compare_result1)
        if set(compare_result1) == set(compare_result2):
            self.textEdit.append("两个文件夹内的文件名称一致，开始比对" + "\n")
            i = 1
            for file_list in compare_result1:
                # path1 = self.lineEdit.text() +"/"+file_list
                path1 = Path(self.lineEdit.text() + "/" + file_list)
                path1 = str(path1).replace("\\", "\\\\")
                # path2 = self.lineEdit_2.text() +"/"+ file_list
                path2 = Path(self.lineEdit_2.text() + "/" + file_list)
                path2 = str(path2).replace("\\", "\\\\")
                self.textEdit.append("<font color=\"#0F0F0F\">旧文件路径：{}</font> ".format(str(path1)))
                # self.textEdit.append("旧文件路径：" + str(path1))
                self.textEdit.append("<font color=\"#0F0F0F\">新文件路径：{}</font> ".format(str(path2)))
                # self.textEdit.append("新文件路径：" + str(path2))
                # print(self.url,self.headers)
                # print("当前文件路径："+path1)
                file_data = {"actual_file": open(path1, 'rb'),
                             "base_file": open(path2, 'rb')}
                result, response = self.cme.test(url=self.url, headers=self.headers, files=file_data)
                print(result)
                if result == 200:
                    self.textEdit.append(
                        "<font color=\"#00FF00\"> Status：{}，两文件内容相同 </font> ".format(str(result)))
                elif result == 417:
                    self.textEdit.append(
                        "<font color=\"#EE2C2C\"> Status：{}-{}，两文件存在差异 </font> ".format(str(result), response))
                else:
                    self.textEdit.append("<font color=\"#0000FF\"> Status：{}，其他错误 </font> ".format(str(result)))
                self.progressBar.setProperty("value", int((i / len(compare_result1)) * 100))
                i += 1
        else:
            self.textEdit.append("文件内容不一致，请检查")
        self.textEdit.append("文件对比完成")

        self.my_str.emit("ok") # 发出任务完成信号

    # def start_thread(self):
    #     """
    #     启动多线程
    #     :return:
    #     """
    #     try:
    #         print("此处省略1万代码")
    #
    #     except Exception as e:
    #         print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
    # self.my_thread.start()
