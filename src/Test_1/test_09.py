# -*- coding:utf-8 -*-  
'''
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
'''
import time
for i in range(10):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)