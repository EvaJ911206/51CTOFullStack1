#!/usr/bin/env python
# -*- coding:utf-8 -*-

#检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
from __future__ import division

def func(args): #函数
    result = [] #新的列表接受返回的结果
    for i in range(len(args)): #循环列表的长度
        if i % 2 == 1: #查找序号为奇数的元素
            result.append(args[i]) #把序号为奇数的元素加入列表中
        else:
            pass
    a = result
    print("奇数的元素：%s" %a)

if __name__ == '__main__': #主程序
    args = [11,22,33,44,55] #输入查找的列表或元组
    func(args) #执行程序
