import chardet
import os

# 获取文件的编码类型
def get_encoding(file_name):
    if file_name.split('.')[1] == 'txt':
        # print(file_name)
        with open(file_name,'rb') as f:
            data = f.read()
            return chardet.detect(data)['encoding']

def get_file_name_list(file_dir):
    for root,dirs,files in os.walk(file_dir):
        return files


file_dir = "D:\桌面文件\\"
filename_list = get_file_name_list(file_dir)
for name in filename_list:
    path = file_dir+name
    # print(path)
    encoding = get_encoding(path)
    print(encoding)
