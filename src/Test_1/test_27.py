# -*- coding:utf-8 -*-  
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
'''
#1
l=['a','d','s','f','h']
t1=l[0]
l[0] = l[4]
l[4]=t1
t2 = l[1]
l[1]=l[3]
l[3]=t2
print(l)

#2
def output(s,l):
    if l==0:
       return
    print (s[l-1])
    output(s,l-1)
 
s = input('Input a string:')
l = len(s)
output(s,l)