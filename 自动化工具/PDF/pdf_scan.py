# -- coding: utf-8 --
# @time :
# @author : 马维畅
# @file : pdf_scan.py
# @software: pycharm

import shutil
import os
from pdfminer.pdfpage import PDFPage

def get_pdf_searchable_pages(fname,fdpath):
    """通过读取PDF文档，是否可以搜索来判断文档是否是扫描件"""
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    try:
        with open(fname, 'rb') as infile:

            for page in PDFPage.get_pages(infile):
                page_num += 1
                if 'Font' in page.resources.keys():
                    searchable_pages.append(page_num)
                else:
                    non_searchable_pages.append(page_num)

        if page_num > 0:
            if len(searchable_pages) == 0:
                shutil.move(fname, fdpath+"\\scan")
                # print(fdpath+"\\pdf-scan")
                print(f"Document '{fname}' has {page_num} page(s). "
                      f"完整文档不可搜索-是扫描件")
            elif len(non_searchable_pages) == 0:
                shutil.move(fname, fdpath+"\\noscan")
                print(f"Document '{fname}' has {page_num} page(s). "
                      f"可搜索完整文档-是非扫描件")
            else:
                shutil.move(fname, fdpath + "\\图文混合")
                print(f"Document '{fname}',searchable_pages : {searchable_pages}")
                print(f"不可搜索页面 : {non_searchable_pages}")
        else:
            shutil.move(fname, fdpath+"\\faild")
            print(f"{fname}Not a valid document")

    except Exception as e:
        shutil.move(fname, fdpath + "\\other")
        print(f"Document '{fname}' has {page_num} page(s). " "Exception: " + str(e))




if __name__ == '__main__':
    folder_path = input("PDF文件夹路径：")
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = folder_path+"\\"+file
        file_path = str(file_path).replace("\\", "\\\\")
        if os.path.isdir(file_path):
            print(f"{file_path}是目录，跳过")
            pass
        else:
            get_pdf_searchable_pages(file_path,folder_path)
