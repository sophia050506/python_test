# -*- coding:utf-8 -*-  
'''
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
'''
#1
l = []
for i in range(1,21):
    num = 1
    for j in range(1,i+1):
        num = num * j
    l.append(num)
   
print(l)
print(sum(l))

#2
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)

#3
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print ('1! + 2! + 3! + ... + 20! = %d' % s)