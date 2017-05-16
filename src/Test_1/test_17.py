# -*- coding:utf-8 -*-  
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
http://www.runoob.com/python/python-exercise-example17.html
'''
#test = 'safdhhfewyr8e8rhrb  8ew rhfjksankdr*^$$'
test = 'runoob'
test_list = list(test)
letter = 0
num  = 0
space = 0
other = 0
for i in range(len(test_list)):
    if test_list[i].isdigit():
        num += 1
    elif test_list[i].isalpha():
        letter += 1
    elif test_list[i].isspace():
        space += 1
    else:
        other += 1
print(letter,num,space,other)        
    
    
