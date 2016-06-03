#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
"""


#函数中，将bool值为0的元素作为空内容进行判断，所以空格不是空内容
def ifnull(obj):
    #判断是否是字符串，元祖或者列表对象
    if isinstance(obj, (str, list, tuple)):
        for i in obj:
            if bool(i) is False:
                print("对象 %s 含有空内容" % str(obj))
                return True
        print("对象 %s 不含有空内容" % str(obj))
    else:
        print("您传入的 %s 不是合法的字符串、列表、元祖对象" % str(obj))
        return False


if __name__ == "__main__":
    pr = """
输入样式：
字符串： "asdf"
元祖：  （1,2,3,4,5）
列表：   [6,7,8,9,10]
    """
    while True:
        print(pr)
        myobj = raw_input("请输入一个对象[字符串，列表或者元祖]：")
        try:
            #对用户输入的字符串求值，获取真正的对象
            myobj = eval(myobj)
        except (SyntaxError, NameError):
            print("您输入的对象不符合语法，请重新输入")
        #如果用户输入无误，则调用ifnull函数
        else:
            ifnull(myobj)
