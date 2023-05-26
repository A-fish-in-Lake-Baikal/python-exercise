# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm
import os

import aspose.words as aw
from datetime import date
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

# PDFJS = 'C:\\Users\\jingj\\Downloads\\pdfjs-3.2.146-dist\\web\\viewer.html'
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'
# PDF = 'D:\TPS\pdf\红头文件2--5页.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        self.file1 = input("PDF1文件夹路径：")
        self.file2 = input("PDF2文件夹路径：")
        super().__init__()
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.load(QtCore.QUrl.fromUserInput(self.compare(self.file1,self.file2)))


    def compare(self,file1,file2):
        # 设置比较选项
        options = aw.comparing.CompareOptions()
        options.ignore_formatting = True
        options.ignore_headers_and_footers = True
        options.ignore_tables = True
        options.ignore_fields = True
        options.ignore_comments = True
        options.ignore_textboxes = True
        options.ignore_footnotes = True
        # 加载PDF文件
        PDF1 = aw.Document(file1)
        PDF2 = aw.Document(file2)
        # 将 PDF 文件转换为docx格式
        PDF1.save("result\\first.docx", aw.SaveFormat.DOCX)
        PDF2.save("result\second.docx", aw.SaveFormat.DOCX)

        # 加载转换后的docx文档
        DOC1 = aw.Document("result\\first.docx")
        DOC2 = aw.Document("result\second.docx")

        # DOC1 对比转换后的文档
        DOC1.compare(DOC2, "user", date.today(), options)

        if (DOC1.revisions.count > 0):
            # 將生成的文件另存为 PDF
            print("Documents are not equal")
            compare_pdf = "result\compared.pdf"
            DOC1.save(compare_pdf, aw.SaveFormat.PDF)
            # self.load(QtCore.QUrl.fromUserInput("result\compared.pdf"))
            path = os.getcwd()+"\\"+compare_pdf
            # print(path)
            return path
        else:
            print("Documents are equal")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())