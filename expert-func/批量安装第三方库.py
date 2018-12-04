# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2018/11/20 21:20
'''
import os

def install():

    libs = {"numpy","matplotlib","pillow","sklearn","pygame","networkx","sympy"}

    for lib in libs:
        try:
            os.system("pip install "+lib)
            print("install successful")
        except:
            print("install failed")




if __name__ == '__main__':
    install()