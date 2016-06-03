#!/usr/bin/env python
# coding:utf-8
# 写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。


def fibonacci(arg):
    """
    :param arg: int
    :return: int
    """
    f1 = 0
    f2 = 1
    if arg == 1:
        return f1
    elif arg == 2:
        return f2
    else:
        fn = fibonacci(arg - 1) + fibonacci(arg - 2)
        return fn
print(fibonacci(10))