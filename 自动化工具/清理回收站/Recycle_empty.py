# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : .py
# @software: pycharm

# 清理回收站
import winshell

try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    print("Recycle bin is emptied Now")
except:
    print("Recycle bin already empty")