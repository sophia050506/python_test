# -*- coding:utf-8 -*-  
'''
题目：文本颜色设置。
程序分析：无。
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[1;31;40m'
    FAIL = '\033[91m'
    ENDC = '\033[1;33;43m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)