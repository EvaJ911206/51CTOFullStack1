#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。


def func1(args):#判断用户输入数据类型：
    for i in r: #循环历遍用户输入数据
        if r.startswith("[") and r.endswith("]"): #判断列表的输入特征
            return "列表"
        elif r.startswith("(") and r.endswith(")"): #判断元组的输入特征
            return "元组"
        elif r.startswith("{") and r.endswith("}"): #判断字典的输入特征
            return "字典"
        elif r.isdigit(): #判断输入是否为数字
            return "数字"
        else:
            return "字符" #其他为字符串


def func2(args):
    if isinstance(args, str) or isinstance(args, list) or isinstance(args, tuple):
    #判断输入是否符合字符，列表，元组属性
        a = len(args) #计算输入数据长度
        print("长度：%s" % a) #输出长度
        if len(args) > 5: #判断长度是否大于5
            print("长度 大于 5") #长度大于5
        else: #长度小于5
            print("长度 小于等于 5")


if __name__ == '__main__': #主程序

    r = input('请输入对象: ')#用户输入数据
    ret = func1(r) #返回结果
    print("数据类型: %s" %ret) #输出数据类型
    func2(r) #执行func2函数

