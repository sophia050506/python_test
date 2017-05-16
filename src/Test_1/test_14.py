# -*- coding:utf-8 -*-  
'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

def element(num):
    l=[]
    for i in range(2,num):
        if num % i == 0:
            l.append(i)
            print(l)
            num = int(num / i)
           

#print(element(90))


def e(n):
    print('{}='.format(n))
    if not isinstance(n, int) or n <= 0:
        print('请输入正确的数字')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for i in xrange(2,n+1):
            if n % i == 0:
                n = int(n / i)
                if n == 1:
                    print(i)
                else:
                    print ('{}*'.format(i))
                break
        
    
#e(-1)
#e(0)
e(1)
e(5)
e(90)
e(100)  
    
    
    