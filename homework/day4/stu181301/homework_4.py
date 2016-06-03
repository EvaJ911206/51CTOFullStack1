#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

#写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。


from sys import exit

def has_space(args):
    for i in args:  # 循环历遍用户输入数据
        if i.isspace():  #判断是否含有空内容'and " " and "[]" and "()" and "{}" in args:' 
            print("输入数据有空内容")
            exit()
        else:
            continue
    print("输入数据没有空内容")

if __name__ == '__main__':  # 主程序
    args = input('请输入数据: ')  # 用户输入数据
    has_space(args)  # 返回结果

