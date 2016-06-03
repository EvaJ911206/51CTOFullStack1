#!/usr/bin/env python
# coding:utf-8
# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。


def isblank(arg):
    """
    :param arg: list | str | tuple
    :return: None
    """
    if isinstance(arg, str) or isinstance(arg, list) or isinstance(arg, tuple):
        string = "".join(arg)
        for i in string:
            if i.isspace():
                print("对象中含有空格")
                break
            else:
                continue
    else:
        print("参数不正确")
ret = ["15454    dasdas", "24"]
isblank(ret)
