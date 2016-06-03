#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

#写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者

# def func(arg1, arg2):
#     if arg1 == 0:
#         print(arg1, arg2)
#     arg3 = arg1 + arg2
#     print(arg3)
#     func(arg2, arg3)
#
# func()


def func(n):
    if n == 0: #第0项是0
        return 0
    elif n == 1:#第1项是第一个1
        return 1
    else:
        #从第三项开始，每一项都等于前两项之和,f(n)+f(n+1)=f(n+2) ==> f(n)=f(n-1)+ f(n-2）
        return func(n-1)+func(n-2)

ret = func(10)
print(ret)




