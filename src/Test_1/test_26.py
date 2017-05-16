# -*- coding:utf-8 -*-  
'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''
#1
s = 1
for i in range(1,6):
    s *= i
print(s)

#2
def fact(j):
    a = 0
    if j == 0:
        a = 1
    else:
        a = j * fact(j - 1)
    return a

for i in range(6):
    print ('%d! = %d' % (i,fact(i)))