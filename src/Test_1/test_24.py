# -*- coding:utf-8 -*-  
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''
#1
l = [1,2]
for i in range(2,21):
    s = l[i-1]+l[i-2]
    l.append(s)
    print(l)
b=[]
for j in range(2,len(l)):
    a = l[j]/l[j-1]
    b.append(a)
    print(b)
print(sum(b))

#2
a = 2
b = 1
lst = []
for i in range(20):
    lst.append(str(a) + '/' + str(b))
    a,b = a+b, a
print('{0} = {1}'.format(eval('+'.join(lst)), '+'.join(lst)))
