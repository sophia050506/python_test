# -*- coding:utf-8 -*-  
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''
def s(num,n):
    s2 = 0
    s = 0
    print('before',s2)
    for i in range(n):
        s1 = num * 10 ** i
        s2 = s2 + s1
        s = s + s2
        print(s1,s2)
    print('s=',s)
s(2, 5)        