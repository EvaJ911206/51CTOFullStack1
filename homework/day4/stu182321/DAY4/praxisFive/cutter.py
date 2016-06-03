#!/usr/bin/env python
# coding:utf-8
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。


def cutter(arg):
    """
    :param arg: list
    :return: list
    """
    string = []
    if isinstance(arg, list):
        if len(arg) > 2:
            string = arg[0:2]
        else:
            string = arg
    else:
        print("参数不正确")
    return string
ret = [12, "11", 13]
print(cutter(ret))
