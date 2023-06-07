# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm

import sys
import zipfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QFileDialog, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file_action = QAction('Open', self)
        open_file_action.setShortcut('Ctrl+O')
        open_file_action.setStatusTip('Open File')
        open_file_action.triggered.connect(self.show_open_dialog)

        save_file_action = QAction('Save', self)
        save_file_action.setShortcut('Ctrl+S')
        save_file_action.setStatusTip('Save File')
        save_file_action.triggered.connect(self.show_save_dialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(open_file_action)
        file_menu.addAction(save_file_action)

        self.setWindowTitle('ZIP Editor')
        self.setGeometry(300, 300, 350, 250)

    def show_open_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Zip File', '', 'Zip Files (*.zip)', options=options)
        if file_name:
            self.open_zip(file_name)

    def open_zip(self, file_name):
        with zipfile.ZipFile(file_name, 'r') as zip_file:
            for name in zip_file.namelist():
                with zip_file.open(name) as myfile:
                    self.text_edit.setPlainText(str(myfile.read(), 'utf-8'))

    def show_save_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Zip File', '', 'Zip Files (*.zip)', options=options)
        if file_name:
            self.save_zip(file_name)

    def save_zip(self, file_name):
        with zipfile.ZipFile(file_name, 'w') as zip_file:
            archive_file_name = 'example.txt'
            zip_file.writestr(archive_file_name, self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())