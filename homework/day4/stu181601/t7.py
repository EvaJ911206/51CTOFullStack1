#! /usr/bin/env python
#-*- coding:utf-8 -*-
#******************************************************
#函数功能：检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#********************************************************

def dictvalcheck2(vel):
    for i in vel.keys():
        a = vel[i][0:2] if len(vel[i]) > 2 else vel[i]
        vel[i] = a
    return vel

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
dic = dictvalcheck2(dic)
print dic
