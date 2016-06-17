#!/usr/bin/python
# -*- coding:utf-8 -*-

import re

num1 = input('请输入运算式：')

#加减乘除运算：这里是借鉴张雨的
def jjcc(strn) :
    li2 = re.findall('[/*]?[\-+]?\d+\.?\d*', strn)      #带符号将字符串中的数字分成列表’
    print(li2[1])
    for i in range(len(li2)):
        if li2[i][0] == '*':    #如果列表完素中含有'*',则当前元素和前一个元素进行乘运算
            li2[i] = li2[i][1:]      #去掉当前元素前的的符号
            li2[i] = str(float(li2[i - 1]) * float(li2[i]))     #转换并运算
            li2[i - 1] = '+0'    #前一个元素用'+0'替换用来占位
        elif li2[i][0] == '/':   #如果列表元素中含有'/',则当前元素和前一个元素行行除运算
            li2[i] = li2[i][1:]      #去掉符号
            li2[i] = str(float(li2[i - 1]) / float(li2[i]))     #和前一个元素运算
            li2[i - 1] = '+0'       #前一个元素用'+0'替换用来占位
    addnum = 0
    for i in li2:   #列表元素都带符号,对列表元素全部进行加运算
        addnum += float(i)
    if addnum >= 0 :
        return "+" + '%.14f'%(addnum)   #将科学计数法转为普通,如果结果为正数,前面补'+'
    else :
        dfd = '%.14f'%addnum  #将科学计数法转为普通,结果不为正,直接转换字符串并返回
        return dfd


#取空格里面的数据
while True:
    num1 = re.sub('\s*', '', num1)   #对输入的内容进行去空格
    result = re.split("\(([^()])\)", num1, 1)   #取最中间的括号内的内容
    if len(result) == 3:
        before,content,after = result   #列表内的内容赋值给不同变量
        r = jjcc(content)     #给计算加减乘除的函数传值
        new_str = before + str(r) + after   #将返回的结果变成str类型，再组合起来
        new_str = new_str.replace("++", "+").replace("+-", "-").replace("--", "+").replace("-+", "-")   #如果有两个符号是一样的情况则统一运算符
        nuw_str = num1  #赋值给变量再次进入循环
    else:
        final = jjcc(num1)   #如果没有括号里的内容了，则把现有的字符串进行加减乘除
        print(final)
        break





