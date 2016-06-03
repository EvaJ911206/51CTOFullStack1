#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
"""


def dictlen(obj):
    tempdict = {}
    if isinstance(obj, dict):
        for key in obj.keys():
            if not isinstance(obj[key], (list, str)):
                print("存在非字符串或者列表的元素值")
                return
            else:
                if len(obj[key]) > 2:
                    tempdict[key] = obj[key][0:2]
                else:
                    tempdict[key] = obj[key]
        print("返回的字典为：%s" % tempdict)
        return tempdict
    else:
        print("您传入的 %s 不是合法的字典对象" % str(obj))
        return


if __name__ == "__main__":
    pr = """
输入样式：
字典：   {"k1": "v1v1", "k2": [11,22,33,44]}
    """
    while True:
        print(pr)
        myobj = raw_input("请输入一个字典对象：")
        try:
            #对用户输入的字符串求值，获取真正的对象
            myobj = eval(myobj)
        except (SyntaxError, NameError):
            print("您输入的对象不符合语法，请重新输入")
        #如果用户输入无误，则调用dictlen函数
        else:
            result = dictlen(myobj)