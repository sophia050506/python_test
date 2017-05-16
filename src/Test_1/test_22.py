# -*- coding:utf-8 -*-  
'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

team_a = ['a','b','c']
team_b = ['x','y','z']
for i in team_a:
    for j in team_b:
        if team_a[i] == 'c' and team_b[j] != 'x' and team_b[j] != 'z':
            if team_a[i] == 'a' and team_b[j] != 'x':
                print(team_a[i],team_b[j])
            else:
                print(team_a[i],team_b[j])
        else:
            print(team_a[i],team_b[j])


'''
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
'''