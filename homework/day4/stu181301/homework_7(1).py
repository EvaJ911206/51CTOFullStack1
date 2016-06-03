#!/usr/bin/env python
# -*- coding:utf-8 -*-

#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#dic = {"k1": "v1v1", "k2": [11,22,33,44]}


def func(args): #函数体
    ret = {} #创建新的字典接受结果
    for key, value in args.items():#循环字典的键和值
        if len(value) > 2:#判断值的长度是否大于2
            ret[key] = value[0:2] #长度大于2，仅保留前两位的值，加入新的字典中
        else:
            ret[key] = value #长度小于2，保留原来的值，加入新的字典中
    return ret #返回新的列表

if __name__ == '__main__': #主函数
    dic = {"k1": "v1v1", "k2": [11,22,33,44]} #导入字典内容
    r = func(dic) #接受返回值
    print(r) # 打印返回值










