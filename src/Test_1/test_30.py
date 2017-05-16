# -*- coding:utf-8 -*-  
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：无。
http://www.runoob.com/python/python-exercise-example30.html
'''
x = int(input("请输入一个数:\n"))
a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)
if a==e and b==d:
    print('回文数')
else:
    print('不是回文数')
    
#2
a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True
for i in range(len(x)/2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print ("%d 是一个回文数!" % a)
else:
    print ("%d 不是一个回文数!" % a)