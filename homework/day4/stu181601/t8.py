#! /usr/bin/env python
# -*- 'coding:utf-8' -*-

#****************************************************************
#功能：利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
#****************************************************************

#编程方法：
#1、描述元素属性： n3=n1+n2
#2、设置环境：v = x + y ，rec(n1,n2),n3 = n1 + n2描述一种环境能够自动向这个模板中输送数据。
#3、环境动起来                    result = rec(n2,n3)

'''def rec(fq,n1,n2):
    if fq > 10:
        return
    n3 = n1 + n2
    print n1
    fqn = fq + 1
    result = rec(fqn,n2,n3)
    return result
    
p = rec(1,0,1)
print p'''

#*********************** function2 *********************************
#将一个正常的函数改为递归,>>>>>>>>>>>>>>>>>>>这样就能达到功能的附加和组合
#      这可以解决类似这种问题：想输出第一第二个数，第三个数为两数之和，第四个数为前两个数之积。向后类推。
def fqc(func):
    def inner(*arg):
        global fq
        
        fq += 1
        if fq >10:
            return
        print 'the %d is '%(fq)
        r = func(arg[0],arg[1])         ###################这里没有想出在最外层函数设置次数的办法。？？？？？？？？？？？？？？？？？？？？？？？？？？？
        return r
    return inner    
def outer(func):
    def inner(*arg):
        n3=arg[0]+arg[1]
        print arg[0]
        rnh = func(0,1)
        print rnh
        r=nh(arg[1],n3)##########这里将nh写入nh此时=inner
        return r
    return inner

@fqc
@outer
def nh(n1,n2):
    n3 = n1+n2
    return 'sum is %d'%(n3)
fq = 0
a = nh(0,1)
print a
    
