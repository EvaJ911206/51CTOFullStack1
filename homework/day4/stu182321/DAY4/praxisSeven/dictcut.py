#!/usr/bin/env python
# coding:utf-8
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""
dic = {"k1": "v1v1", "k2": [11,22,33,44]}

PS:字典中的value只能是字符串或列表
"""


def dictcut(arg):
    """
    :param arg: dict
    :return: dict
    """
    if isinstance(arg, dict):
        for item in arg.keys():
            if isinstance(arg[item], str) or isinstance(arg[item], list):
                if len(arg[item]) > 2:
                    arg[item] = arg[item][0:2]
                else:
                    continue
            else:
                continue
    else:
        print("传入正确的参数")
    return arg
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
print(dictcut(dic))
