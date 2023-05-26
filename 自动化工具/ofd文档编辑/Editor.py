# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget,QMenuBar,QFileDialog
from PyQt5.QtGui import QPalette, QColor

from Base.edit_file import EditFile
from Main_Ui import Ui_MainWindow
from PyQt5.QtCore import Qt
class Editor_Main(QMainWindow):
    def __init__(self, parent=None):
        super(Editor_Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actiondakd.triggered.connect(self.open_file)
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
    def close_tab(self, index):
        """关闭tab"""
        if index > 0 and index < self.ui.tabWidget.count():
            # check if index is valid
            self.ui.tabWidget.removeTab(index)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, '打开文件', '', 'Text Files (*.txt);;All Files (*)')
        print("选择的文件为：{}\n".format(file_path))
        EditFile.OpenFile(file_path)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        mywindow = Editor_Main()
        palette = QPalette()
        # palette.setColor(QPalette.Window, QColor(0, 0, 255))  # 这里设置为蓝色
        # palette.setColor(QPalette.windowText,QColor(255,255,255))
        # mywindow.setStyleSheet('QWidget{border: 2px solid red; background-color: yellow;}')
        mywindow.setPalette(palette)
        mywindow.show()
        sys.exit(app.exec_())
    except Exception as ex:
        print("Error:", ex)
