# -*- coding:utf-8 -*-  
'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
def fib1(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fib2(n):
    if n==1 :
        return 0
    if  n==2:
        return 1
    return fib2(n-1)+fib2(n-2)

def fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [1, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
# 输出了第10个斐波那契数列
print (fib2(10))  