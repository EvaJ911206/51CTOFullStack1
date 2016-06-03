#!/usr/bin/env python
# -*- coding:utf-8 -*-

#2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
from __future__ import division

from sys import exit #导入sys模块的exit函数


def read_line(args):#把用户输入的字符串拷贝到文本文件中
    with open('input.log', "w+") as f:#以写读模式打开文件
        f.write(r) #写入用户输入的字符串
        f.seek(0) #设定指针到文件开头
        data = f.read()#读取文件内容
    # print("您输入的字符串：%s" %data) #显示用户输入内容
        a = input("请检查输入内容%s \n Y/y 确定, N/n 退出程序" %data)#用户判断输入内容，
        while True:
            if a.lower().strip() == 'y': #‘y’继续程序判读操作
                break
            elif a.lower().strip() == 'n':#‘n’退出程序
                exit(5)


#写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def func1(s):
    alphard_num = 0 #设定字母的初始值为0
    space_num = 0 #设定空格的初始值为0
    digit_num = 0 #设定数字的初始值为0
    other_num = 0 #设定其他字符串的初始值为0

    for i in s:
        if i.isdigit(): #判断是否为数字
            digit_num += 1 #统计数字加1
        elif i.isspace(): #判断是否为空格
            space_num += 1  #统计空格加1
        elif i.isalpha(): #判断是否为字母
            alphard_num += 1 #统计字母加1
        else:
            other_num += 1 #其他字符串加1
    return ("统计结果 字母：%d 个 ,空格：%d 个, 数字：%d 个, 其他字符：%d 个" % (alphard_num, space_num, digit_num, other_num))
    #返回统计结果

if __name__ == '__main__': #主程序

    r = input('请输入字符串: ')#用户输入
    read_line(r) #以用户输入内容为参数执行read_line()函数
    ret = func1(r) #返回结果
    print(ret) #打印返回结果


