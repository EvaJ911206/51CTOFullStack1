#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

import re

def deal_minus_issue(calc_list):#
    """

    :param calc_list: 先去除出+-号后，重新拼接排列算式
    :return: 返回已经重新排列算式
    """
    new_calc_list = [] #新列表整理乘除的元素替换旧列表
    for index, item in enumerate(calc_list): #循环元素
        if item.strip().endswith("*") or item.strip().endswith("/"): #以乘除结尾的元素如'2*5/', '3',合并起来
            new_calc_list.append("%s-%s" %(calc_list[index], calc_list[index+1]))#重新把数字和*/符号拼接起来
        elif ("*" or "/") in item: #去除不含*/的元素
            new_calc_list.append(item)#加入新的列表中
    return new_calc_list #返回新的列表


def mutilpy_and_dividend(formula):#乘除计算
    """

    :param formula: 计算乘除
    :return: 返回乘除的结果
    """
    calc_list = re.split("[+-]", formula)#用+-号分裂算式，
    calc_list = deal_minus_issue(calc_list)#重新拼接等式
    for item in calc_list:#
        sub_calc_list = re.split("[*/]", item)#用*/号分裂算式，得到数字字符
        sub_operator_list = re.findall("[*/]", item)#寻找*/号，得到符号列表
        sub_res = None #默认结果为空字符
        for index, i in enumerate(sub_calc_list):#循环数字字符的位置和字符
            if sub_res:#若已经有第一个值后
                if sub_operator_list[index-1] == "*": #若符相对符为*号，
                    sub_res *= float(i) #与前一个数相乘
                else:#加入第一个值
                    sub_res /= float(i) #非*为除
            else:#加入第一个值
                sub_res = float(i)
        formula = formula.replace(item, str(sub_res))#再把计算结果与原来的算式替换，组成新的算式
    sub_process(formula)
    return formula#返回

def sub_process(formula):
    """

    :param formula: 加减法
    :return: 返回最后结果
    """

    sub_calc_list1 = re.split("[+-]", formula)#用+-号分裂算式生成新列表
    sub_operator_list1 = re.findall("[+-]", formula) #找出+-号生成新的列表
    sub_res1 = None #结果默认为空
    for index, item in enumerate(sub_operator_list1): #循环+-符号列表
        for index2, item2 in enumerate(sub_calc_list1): #循环算式生成新列表
            if sub_res1: #非第一次加入计算
                if sub_operator_list1[index - 1] == "-": #+-符号列表的位置减一为减号的计算符号
                    sub_res1 -= float(item2)#与前一个数字相减
                else:
                    sub_res1 += float(item2) #与前一个数字相加
            else:#首次加入数字
                sub_res1 = float(item2) #
        return sub_res1 #返回最后结果

def calc(formula):
    """

    :param formula: 去括号
    :return:
    """
    parentheses_flag = True #有括号
    while parentheses_flag:#
        m = re.search("\([^()]+\)", formula)#匹配括号
        if m:#若有括号
            print(m.group())
            sub_formula = m.group().strip("()")#去括号
            formula = mutilpy_and_dividend(sub_formula)#运算乘除
            sub_res = sub_process(formula)#运算加减
            print(sub_res)#结果
        break

if __name__ == "__main__":
    formula = "(9-2*5/3+7/3*99/4*2998+10*568/14)"
    res = calc(formula)