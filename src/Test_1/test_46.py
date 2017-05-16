# -*- coding:utf-8 -*-  
'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
程序分析：无
'''

x = int(input('请输入数字：'))
s = x*x
if s < 50:
    print('您输入的数字过小！')
    exit
else:
    print(s)





