#! /usr/bin/env python
#-*- coding:utf-8 -*-
#******************************************************
#函数功能：检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#********************************************************
#****************************function 1 *******************************************
def listcheck2(vel):
    col = []
    listlen = len(vel)
    for i in range(0,listlen,2):
        print i
        col.append(vel[i])
    
    return col

lis = [11,22,33,44,55]
lis = listcheck2(lis)
print lis

tu = (11,22,'33','qwe',55)
tu = listcheck2(tu)
print tu

#****************************function 2 *******************************************
def listcheck2(vel):
    col = vel[::2]    
    return col

lis = [11,22,33,44,55,66,77,88,99]
lis = listcheck2(lis)
print lis

tu = (11,22,'33','qwe',55,66,'qw','t','','t')
tu = listcheck2(tu)
print tu
