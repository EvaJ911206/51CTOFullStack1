#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
"""


def oddlist(obj):
    #判断是否是列表或者元祖对象
    if isinstance(obj, (list, tuple)):
        #通过列表生成式返回对象的奇数位索引对应的元素
        ret = [obj[x] for x in range(len(obj)) if x % 2 == 1]
        print("返回的奇数位索引元素为：%s" % ret)
        return ret
    else:
        print("您传入的 %s 不是合法的列表或者元祖对象" % str(obj))
        return


if __name__ == "__main__":
    pr = """
输入样式：
元祖：   [1,2,3,4,5]
列表：   [6,7,8,9,10]
    """
    while True:
        print(pr)
        myobj = raw_input("请输入一个列表或者元祖对象：")
        try:
            #对用户输入的字符串求值，获取真正的对象
            myobj = eval(myobj)
        except (SyntaxError, NameError):
            print("您输入的对象不符合语法，请重新输入")
        #如果用户输入无误，则调用oddlist函数
        else:
            result = oddlist(myobj)