#!/usr/bin/evn python
#-*- coding:utf-8 -*-
#8、写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。


def fib(a,b,n):
    if n == 10 :  #边界条件
        return a #如果到了第10个数值，返回
    n = n + 1
    c = a + b
    t = fib(b,c,n) #递归
    return t
re = fib(0,1,1)
print(re)
