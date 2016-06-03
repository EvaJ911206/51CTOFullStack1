#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者
"""


#定义斐波那契数列，数列第一个元素为0，第二个元素为1，后面所有的元素为其前面两个元素相加的值
def fib(n):
    if not (n >= 0 and isinstance(n, int)):
        print("入参必须为正整数")
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


result = fib(10)
print("斐波那契数列的第十个元素为：%s" % result)