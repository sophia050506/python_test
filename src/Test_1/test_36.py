# -*- coding:utf-8 -*-  
'''
题目：求100之内的素数。
程序分析：无。
'''
for num in range(1,100):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
