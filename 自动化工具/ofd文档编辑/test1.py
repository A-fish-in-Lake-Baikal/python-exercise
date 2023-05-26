# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm
import sys
import asyncio
import zipfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.openAction = QAction('打开', self)
        self.openAction.triggered.connect(self.openFile)

        self.saveAction = QAction('保存', self)
        self.saveAction.triggered.connect(self.saveFile)

        self.toolbar = self.addToolBar('工具栏')
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.editText = QTextEdit(self)
        self.setCentralWidget(self.editText)

    async def loadZipFile(self, filePath):
        with zipfile.ZipFile(filePath) as zipFile:
            for name in zipFile.namelist():
                with zipFile.open(name) as file:
                    content = await file.read()
                    print(content)
                    self.editText.insertPlainText(content.decode())

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, '打开文件', '', 'Zip文件 (*.zip)')
        if filePath:
            asyncio.run(self.loadZipFile(filePath))

    def saveFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '保存文件', '', 'Zip文件 (*.zip)')
        if filePath:
            with zipfile.ZipFile(filePath, 'w') as zipFile:
                content = self.editText.toPlainText().encode()
                zipFile.writestr('content.txt', content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
