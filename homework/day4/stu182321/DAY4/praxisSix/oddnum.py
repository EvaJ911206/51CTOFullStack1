#!/usr/bin/env python
# coding:utf-8
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。


def oddnum(arg):
    """
    :param arg: list | tuple
    :return: list
    """
    string = []
    if isinstance(arg, list) or isinstance(arg, tuple):
        for i in range(len(arg)):
            if i % 2 == 1:
                string.append(arg[i])
            else:
                pass
            i += 1
    else:
        print("输入的参数不正确")
    return string
ret1 = ["你好", "hello", "12", 12]
print(oddnum(ret1))
ret2 = ("你好", "hello", "12", 12, 15, "Python")
print(oddnum(ret2))
