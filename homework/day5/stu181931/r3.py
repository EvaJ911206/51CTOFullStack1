#!/usr/bin/evn python
#-*- coding:utf-8 -*-
def outer(func):
    def inner(*args,**kwargs):
        print('123')
        ret = func(*args,**kwargs)
        print('456')
        return ret
    return inner

@outer
def index1(a1,a2):
    print('原来的函数')
    return a1 + a2

index1(1,2)

"""
1:  解释器从上向下执行。在内存先创建outer函数。 函数内部未执行。
2： 创建index函数。
3： 执行index 和outer的联合。
4： 执行outer函数，将index作为参数传递给outer。
5： 在传递参数给outer的时候，创建func函数。所以outer 也指向index 。
6:  执行outer内的inner。创建inner函数。
7： 在函数inner内部，func 指向原来的index函数。
8： inner函数是新的index函数。

执行步骤：
1：执行index（）
2：执行outer 内部函数的inner。
3：在inner 内部，执行print（123）调。用原来index。
4：执行原来的index。
5：执行完毕原来的index 后，返回inner 内部。
6：执行inner 剩下的步骤。
7：inner 执行完毕，返回相关的返回值。

执行index（）的时候，执行的是新的index，也就是outer 内部的inner
"""
