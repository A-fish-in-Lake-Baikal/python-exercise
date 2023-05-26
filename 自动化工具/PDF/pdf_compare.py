# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : pdf_compare.py
# @software: pycharm

# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : pdf_compare.py
# @software: pycharm

import aspose.words as aw
from datetime import date
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

class Compare_PDF(object):
    def __init__(self):
        # pdf.js选项
        super().__init__()
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)

        # 设置比较选项
        self.options = aw.comparing.CompareOptions()
        self.options.ignore_formatting = True
        self.options.ignore_headers_and_footers = True
        self.options.ignore_case_changes = True
        self.options.ignore_tables = True
        self.options.ignore_fields = True
        self.options.ignore_comments = True
        self.options.ignore_textboxes = True
        self.options.ignore_footnotes = True
    def compare(self,file1,file2):
        # 加载PDF文件
        PDF1 = aw.Document(file1)
        PDF2 = aw.Document(file2)
        # 将 PDF 文件转换为docx格式
        PDF1.save("result\\first.docx", aw.SaveFormat.DOCX)
        PDF2.save("result\second.docx", aw.SaveFormat.DOCX)

        # 加载转换后的docx文档
        DOC1 = aw.Document("first.docx")
        DOC2 = aw.Document("second.docx")

        # DOC1 对比转换后的文档
        DOC1.compare(DOC2, "user", date.today(), self.options)

        if (DOC1.revisions.count > 0):
            # 生成的文件另存为 PDF
            print("Documents are not equal")
            DOC1.save("result\compared.pdf", aw.SaveFormat.PDF)
            self.load(QtCore.QUrl.fromUserInput("result\compared.pdf"))
        else:
            print("Documents are equal")

if __name__=='__main__':
    com = Compare_PDF()
    file1 = input("PDF1文件夹路径：")
    file2 = input("PDF2文件夹路径：")
    com.compare(file1,file2)
    app = QtWidgets.QApplication(sys.argv)
    # window = Window()
    com.setGeometry(600, 50, 800, 600)
    com.show()
    sys.exit(app.exec_())

