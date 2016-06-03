#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def func(args):
    if isinstance(args, list):#判断输入数据是否为列表
        r = len(args) #计算列表长度
        print("列表长度：%s" %r) #输出列表长度
        if len(args) > 2: #条件长度大于2
            del args[2:] #删除切片前两位后的数字
            print(args) #打印出来
        else:
            print("列表长度小于2") #小于长度2
    else:
        print("列表输入有误！") #非列表，输出“输入的列表有误”


if __name__ == '__main__': #主程序
    li = [11,22,33,44,55]
    func(li)



