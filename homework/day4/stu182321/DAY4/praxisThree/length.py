#!/usr/bin/env python
# coding:utf-8
# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。


def length(arg):
    """
    :param arg: list | str | tuple
    :return: None
    """
    if isinstance(arg, str) or isinstance(arg, list) or isinstance(arg, tuple):
        if len(arg) > 5:
            print("该对象的长度大于5")
        else:
            print("该对象的长度不大于5")
    else:
        print("传入参数不正确")

ret = "老男孩Python培训"
length(ret)
