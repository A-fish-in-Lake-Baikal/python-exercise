# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm
import asyncio
import sys
import zipfile
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTabWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
class ZipFileEditor(QObject):
     file_changed = pyqtSignal(str)
     def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.zip_file = None
        self.file_content = {}
     async def open(self):
        self.zip_file = zipfile.ZipFile(self.path, 'a')
        for info in self.zip_file.infolist():
            if not info.filename.endswith('.txt'):
                continue
            with self.zip_file.open(info) as file:
                loop = asyncio.get_event_loop()
                content = await loop.run_in_executor(None, file.read)
                self.file_content[info.filename] = content.decode()
        self.zip_file.close()
     def save(self, path: str):
        with zipfile.ZipFile(path, 'w') as new_zip_file:
            for info in self.zip_file.infolist():
                with self.zip_file.open(info) as file:
                    data = file.read()
                    if info.filename.endswith('.txt'):
                        # 替换该文件为新的内容
                        new_zip_file.writestr(info, self.file_content[info.filename])
                    else:
                        # 不需要修改的文件原样写入新 ZIP 文件中
                        new_zip_file.writestr(info, data)

     def close(self):
        self.zip_file.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建菜单栏
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('文件')
        # 添加“打开”菜单项并绑定事件处理函数
        open_action = file_menu.addAction('打开')
        open_action.triggered.connect(self.async_open_zip_file)

        # 添加“保存”菜单项并绑定事件处理函数
        save_action = file_menu.addAction('保存')
        save_action.triggered.connect(self.save_zip_file)

        # 创建文本编辑框
        self.text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_edit)
         # 初始化文件编辑器为 None
        self.editor = None
    # def open_zip_file(self):
        # def on_open_zip_file(await_coroutine=None):
        #     await_result = await_coroutine.result()
        #     for filename, content in self.editor.file_content.items():
        #         self.add_tab(filename, content)
    async def async_open_zip_file(self):
        await self.editor.open()
        # on_open_zip_file()
        # 打开 ZIP 文件选择对话框
        path, _ = QFileDialog.getOpenFileName(
            self, '打开 ZIP 文件', '', 'ZIP Files (*.zip);;All Files (*)')
        if not path:
                return
             # 关闭上一个编辑器（如果有的话）
        if self.editor:
            self.editor.close()

        # 创建新的文件编辑器，并在异步任务中加载 ZIP 文件中所有文本文件的内容
        self.editor = ZipFileEditor(path)
        await self.editor.open()

        # 将 ZIP 文件中所有文本文件的内容显示到文本编辑框中
        for filename, content in self.editor.file_content.items():
            self.add_tab(filename, content)
    def add_tab(self, title, content):
        text_edit = QtWidgets.QTextEdit()
        text_edit.setText(content)
        text_edit.textChanged.connect(self.update_content)
        self.text_edit.addTab(text_edit, title)

    def update_content(self):
        current_index = self.text_edit.currentIndex()
        title = self.text_edit.tabText(current_index)
        new_content = self.text_edit.currentWidget().toPlainText()
        self.editor.file_content[title] = new_content

    def save_zip_file(self):
        if self.editor is None:
            return

        # 打开 ZIP 文件保存对话框
        path, _ = QFileDialog.getSaveFileName(
            self, '保存 ZIP 文件', '', 'ZIP Files (*.zip);;All Files (*)')
        if not path:
            return

        # 保存更改到新的 ZIP 文件中
        self.editor.save(path)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
