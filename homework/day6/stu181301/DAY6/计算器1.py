#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division


import re
# origin2 = "1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)"

# def replace_func(args):





def add_sub(args):

    # if args.__contains__()

    #\d+\.*\d*[\+\-]{1}\d+\.*\d*
    add_sub1 = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', args).group()
    # replace_sub = re.split("[]")
    # res4 = re.search('\d+\.?\d+[+-]\d+\.?\d+', args).group()
    print("add_sub1", add_sub1)

    if add_sub1:

        before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', args, 1)
        print(before, type(before))

        if "+" in add_sub1:
            n1, n2 = add_sub1.split("+")
            val = str(float(n1) + float(n2))
            # print(val, type(val))
            # val = str(val)
            # print(val, type(val))
            # new_res = before + val + after
            # print(new_res, type(new_res))

        else:
            n1, n2 = add_sub1.split("-")
            val = str(float(n1) - float(n2))

        add_sub1_res = before + val + after
        print("add_sub1_res", add_sub1_res, type(add_sub1_res))
        # caculateable(new_res)

        add_sub1_res1 = re.findall("[+-]", add_sub1_res)
        # if ("+" or "-") in add_sub1_res:
        if add_sub1_res1:
            print("add_sub1_res", add_sub1_res)
            new_add_sub_res = add_sub(add_sub1_res)
            return new_add_sub_res
        else:
            # r = caculateable(new_res)
            print("ok")
            # new_add_sub_res = add_sub(add_sub1_res)
            # return new_add_sub_res
            return add_sub1_res
    else:
        return
        # print("add_sub")
        # arg = add_sub(args)
        # print(add_sub1)
        # caculateable(args)
    #

def mut_div(args): #计算函数

    mut_div1 = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', args).group()
    if mut_div1:
    # if not mut_div1:
    #     args = mut_div(args)
    #     return args
        # before, after = re.split('[*/]', args, 1)
        before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', args, 1)
        print("before", before, "after", after)
        if "*" in mut_div1:
            n1, n2 = mut_div1.split("*")
            val = str(float(n1) * float(n2))
        elif "/" in mut_div1:
            n1, n2 = mut_div1.split("/")
            val = str(float(n1) / float(n2))

        mut_div_res = before + val + after
            # print(val, type(val))
            # val = str(val)
            # print(val, type(val))
            # new_res = before + val +after
            # print(new_res, type(new_res))
        print("mut_div_res", mut_div_res, type(mut_div_res))
        mut_div_res1 = re.findall("[*/]", mut_div_res)
        if mut_div_res1:
        # if ("/" or "*") in mut_div_res:
        # for i in mut_div_res:
        #     if i == "*" or "/":
                # mut_div(mut_div_res)
            print("new_mut_res")
            new_mut_res = mut_div(mut_div_res)
            return new_mut_res
        else:
            # r = caculateable(new_res)
            print("ok")
            add_sub_res = add_sub(mut_div_res)
            # caculateable(mut_div_res)
            return add_sub_res
            # return new_res
    else:
        print("No")
        add_sub_res = add_sub(args)
        return add_sub_res
        # add_sub(args)


def caculateable(args):

    # comput_math = re.search('\d+\.?\d+[*/|+-]\d+\.?\d+', args)
    comput_math = re.findall('[*/+-]', args)
    print(args)

    if comput_math:
        if ("*" or "/") in comput_math:
            sub_r = mut_div(args)
            return sub_r
        # # elif "*" or "/" not in comput_math:
        elif ("+" or "-") in comput_math:
        #     # "+" or "-" in comput_math:
            print("add_sub")
            sub_r = add_sub(args)
            print("r", sub_r)
            return sub_r
    else:
        # args = caculateable(args)
        return args


origin2 = "4*5-(100+2*3*50/5+100-20)*5/2+(50*2-60+100)"
# origin2 = "(100+100-100+100+100+100)"

while True:

    print(origin2)
    result = re.split("\(([^()]+)\)", origin2, 1)
    print("result", result)
    if len(result) == 3:
        before, content, after = result
        sub_r = caculateable(content)
        new_str = before + str(sub_r) + after
        origin2 = new_str
    else:
        f_result = caculateable(origin2)
        print(f_result)
        break


# add_sub(res1)

res1 = "(100+100-100+100+100+100)"


