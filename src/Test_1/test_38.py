# -*- coding:utf-8 -*-  
'''
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''
matrix = [[4,5,6],[7,8,9],[1,2,3]]
s = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            s += matrix[i][j]
            print( matrix[i][j] , i ,j )
print(s)            
