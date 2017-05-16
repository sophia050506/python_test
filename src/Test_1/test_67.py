# -*- coding:utf-8 -*-  
'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
程序分析：无。
'''
a = [3,5,9,34,54,1,12]
for i in range(len(a)):
    if a[i] == max(a):
        a[0],a[i] = a[i],a[0]

for i in range(len(a)):
    if a[i] == min(a):
        a[len(a)-1],a[i]=a[i],a[len(a)-1]
print(a)        