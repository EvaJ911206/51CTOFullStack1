#!/usr/bin/evn python
#-*- coding:utf-8 -*-
def outer_0(func):
    def inner(*args, **kwargs):
        print('最外层装饰器')
        ret = func(*args, **kwargs)
        print('执行完外层装饰器')
        return ret
    return inner


def outer(func):
    def inner(*args, **kwargs):
        print('里层装饰器')
        ret = func(*args, **kwargs)
        print('执行完里层装饰器')
        return ret
    return inner


@outer_0
@outer
def index(a,b):
    print('我是原函数')
    return a + b

t = index(1,2)
print(t)

"""
内部流程：
1: 解释器从上向下执行，将outer_0，outer 均在内存中创建函数。
2：创建index函数。
3：绑定@outer和index 作为@outer_0的参数。传递给outer_0 。 outer_0 会把inner 重新赋值给绑定的@outer 和index
4: 所以outer_0 内部的inner = @outer的inner的合并
5：@outer和inner的合并，本质上是 ouer内部 inenr函数重新赋值给index。
6：所以相当于给outer内部的inner 添加上了@outer_0的装饰器。或者说 将 outer_0 的inner 重新赋给 outer 的inner
 也就重新赋值给了index


执行步骤：
1：在执行index(),先执行最外层装饰器的inner函数。
2：执行outer_0 的 inner函数内部的func函数。
3：上步骤的func指的是内层装饰器的iner函数。
4：执行outer的inner函数内部的 func函数。
5：步骤4的func 指的是原函数index
6：执行原函数index
7：执行完原源函数index后，回到步骤4，执行outer 的inner 函数 剩下的步骤。print 和return操作。
8：执行完outer 的inner函数后，回到步骤4，执行outer_0 的inner函数，剩下的步骤。print 和return 操作。
9：执行完毕
"""
