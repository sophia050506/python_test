# -*- coding:utf-8 -*-  
'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

星期一： Mon.=Monday 
星期二： Tues.=Tuesday 
星期三： Wed.=Wednesday 
星期四： Thur.=Thursday 
星期五： Fri.=Friday 
星期六： Sat.=Saturday 
星期天： Sun.=Sunday
'''
first_letter = input('请输入第一个字母')
day = ''
if first_letter == 'M' or first_letter == 'm':
    day = '星期一'
elif first_letter == 't' or first_letter == 'T':
    second_letter = input('请输入第二个字母')
    if second_letter == 'u' or second_letter == 'U':
        day = '星期二'
    elif second_letter == 'h' or second_letter == 'H':
        day = '星期四'
    else:
        day = '输入有误'
elif first_letter == 'w' or first_letter == 'W':
    day = '星期三'
elif first_letter == 'f' or first_letter == 'F':
    day = '星期五'
elif first_letter == 's' or first_letter == 'S':
    second_letter = input('请输入第二个字母')
    if second_letter == 'a' or second_letter == 'A':
        day = '星期六'
    elif second_letter == 'u' or second_letter == 'U':
        day = '星期天'
    else:
        day = '输入有误'
else:
        day = '输入有误'
print(day)    
    
