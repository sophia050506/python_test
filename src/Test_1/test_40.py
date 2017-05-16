# -*- coding:utf-8 -*-  
'''
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
'''
#1
l = [11,15,25,36,56,42,48,1,9,98,77]
print(l[::-1])


#2
a = [9,6,5,4,1]
N = len(a) 
print (a)
for i in range(len(a) / 2):
    a[i],a[N - i - 1] = a[N - i - 1],a[i]
print (a)




