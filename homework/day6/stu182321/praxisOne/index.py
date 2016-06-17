#!/usr/bin/env python
# coding:utf-8
"""
计算形如字符串"1 - 2 * ((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"的结果
"""
import re


def compute(args):
    """
    计算字符串的值re
    :param args: str 待运算的字符串
    :return: str 计算结果字符串
    """
    args = re.sub("\s+", "", args)
    result = re.split("(\+|-|\*|/)", args)
    while "" in result:
        i = result.index("")
        result[i+2] = "".join([result[i+1], result[i+2]])
        del result[i]
        del result[i]
    while "*" in result or "/" in result:
        for index, item in enumerate(result):
            if item == "*":
                result[index - 1] = float(result[index - 1]) * float(result[index + 1])
                del result[index], result[index]
            elif item == "/":
                result[index - 1] = float(result[index - 1]) / float(result[index + 1])
                del result[index], result[index]
    while "+" in result or "-" in result:
        for index, item in enumerate(result):
            if item == "+":
                result[index - 1] = float(result[index - 1]) + float(result[index + 1])
                del result[index], result[index]
            elif item == "-" and index != 0:
                result[index - 1] = float(result[index - 1]) - float(result[index + 1])
                del result[index], result[index]

    return str(result[0])


def spilt_num(args):
    """
    计算器
    :param args: str 待计算的字符串
    :return: str 计算结果
    """
    flag = True
    while flag:
        result = re.split("\(([^()]+)\)", args, 1)
        if len(result) == 3:
            result[1] = compute(result[1])
            args = "".join(result)
        else:
            flag = False
    return compute(args)


if __name__ == '__main__':
    origin = "1 - 2 * ((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
    print(spilt_num(origin))
