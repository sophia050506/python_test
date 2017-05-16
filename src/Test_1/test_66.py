# -*- coding:utf-8 -*-  
'''
题目：查找字符串。　　
程序分析：无。
'''
n1 = int(input('请输入数字1'))
n2 = int(input('请输入数字2'))
n3 = int(input('请输入数字3'))

if n1>n2:
    n1,n2 = n2,n1
if n1>n3:
    n1,n3 = n3,n1
if n2>n3:
    n2,n3 = n3,n2
print(n1,n2,n3)    

