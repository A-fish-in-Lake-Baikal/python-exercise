# -*- coding: UTF-8 -*-
import xlrd
import os

file_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(file_path, 'xl.xls')
book = xlrd.open_workbook(base_path)
sheet1 = book.sheets()[2]
nrows = sheet1.nrows
print('表格总行数', nrows)
ncols = sheet1.ncols
print('表格总列数', ncols)
row3_values = sheet1.row_values(2)
print('第3行值', row3_values)
col3_values = sheet1.col_values(2)
print('第3列值', col3_values)
cell_3_3 = sheet1.cell(7, 9).value
print('第3行第3列的单元格的值：', cell_3_3)