#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
"""


def iflistandlen(obj):
    #判断是否是列表对象
    if isinstance(obj, (list,)):
        if len(obj) > 2:
            obj = obj[0:2]
            print("返回的对象为：%s" % str(obj))
            return obj
        else:
            print("对象长度不足")
            return obj
    else:
        print("您传入的 %s 不是合法的列表对象" % str(obj))
        return


if __name__ == "__main__":
    pr = """
输入样式：
列表：   [6,7,8,9,10]
    """
    while True:
        print(pr)
        myobj = raw_input("请输入一个列表对象：")
        try:
            #对用户输入的字符串求值，获取真正的对象
            myobj = eval(myobj)
        except (SyntaxError, NameError):
            print("您输入的对象不符合语法，请重新输入")
        #如果用户输入无误，则调用iflistandlen函数
        else:
            result = iflistandlen(myobj)
            # print("-"*50)
            # print("获取的函数返回为：%s" % result)

