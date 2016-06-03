#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
"""
#从string类中导入2个属性，一个是全部数字，一个是全部字母
from string import digits, ascii_letters


def CharStatics(string):
    #定义初始的结果字典,
    result = {"num": [0, ""], "alpha": [0, ""], "blank": [0, ""], "other": [0, ""]}
    #逐一判断传入字符串的每个字符是数字，字母，空格，还是其他
    for i in string:
        if i in digits:
            #递增统计的总数
            result["num"][0] += 1
            #满足条件的字符加入到返回的结果字符串中
            result["num"][1] += i
        elif i in ascii_letters:
            result["alpha"][0] += 1
            result["alpha"][1] += i
        elif i in " ":
            result["blank"][0] += 1
        else:
            result["other"][0] += 1
            result["other"][1] += i
    print("您传入的字符串为： %s" % string)
    print("数字个数： %s  数字为： %s" % (result["num"][0],result["num"][1]))
    print("字符个数： %s  字符为： %s" % (result["alpha"][0],result["alpha"][1]))
    print("空格个数： %s" % result["blank"][0])
    print("其他字符个数：%s  其他字符为：%s" % (result["other"][0],result["other"][1]))


if __name__ == "__main__":
    #获取用户输入内容
    while True:
        userinput = raw_input("请输入内容：")
        CharStatics(userinput)
        print('-' * 50)