# -- coding: utf-8 --
import comtypes.client
import os
def ppt_to_pdf():
    #设置路径
    input_file_path=os.path.abspath("xl.xlsx")
    output_file_path=os.path.abspath("xls.pdf")
    #创建PDF
    powerpoint=comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible=1
    slides=powerpoint.Presentations.Open(input_file_path)
    #保存PDF
    slides.SaveAs(output_file_path,32)
    slides.Close()