#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

def func(args): #函数体
    for key, value in args.items(): #循环函数的键和值
        if len(value) > 2: #判断值的长度是否大于2
            args[key] = value[0:2] #长度大于2，仅保留前两位的值
        else:
            args[key] = value #长度小于2，保留原来的值

if __name__ == '__main__':
    dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]} #导入字典
    func(dic)#执行函数
    print(dic)#打印字典

