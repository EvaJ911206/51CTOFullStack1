#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division


import re
# origin2 = "1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)"

# def replace_func(args):


def sub_process(args):

    sub_process_check = re.findall(r"\+\+|--", args)
    if "--" or "++" in sub_process_check:

        new_formual = re.sub("\+\+|--", "+", args)
        print(new_formual)
        return new_formual

    else:
        # print(args)
        return (args)
    # new_list = []
    # sub_check = re.search("[+-],[--],[-+],[++]", args, 1)
    #
    # if sub_check:
    #     sub_check = re.findall("[+-],[--],[-+],[++]", args)
    #     print("True", sub_check)
    #     # else:
    #     #     return args
    # else:
    #     # print()
    #     return args

def add_sub(args):

    pre_formula = args
    # if "+-" or "-+" or "--" or "++" in args:
    sub_formula = sub_process(pre_formula)
    #\d+\.*\d*[\+\-]{1}\d+\.*\d*
    add_sub1_check = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', sub_formula)
    print("add_sub1_check", add_sub1_check)

    if add_sub1_check:
        add_sub1 = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', sub_formula).group()
        split_formula = re.split("([+-])", add_sub1, 1)
        if split_formula[1] == "+":
            val = str(float(split_formula[0]) + float(split_formula[2]))
        else:
            val = str(float(split_formula[0]) - float(split_formula[2]))
        before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', add_sub1)
        print(before, after)
        new_formula = "%s%s%s" % (before, val, after)
        print("new_formula", new_formula)
        args = new_formula
        new_result = add_sub(args)
        return new_result

    else:
        print("add_sub_final", args)
        return args

    # before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', args, 1)
    # print(before, type(before))
    #
    # if "+" in add_sub1:
    #     n1, n2 = add_sub1.split("+")
    #     val = str(float(n1) + float(n2))
    #     # print(val, type(val))
    #     # val = str(val)
    #     # print(val, type(val))
    #     # new_res = before + val + after
    #     # print(new_res, type(new_res))
    #
    # else:
    #     n1, n2 = add_sub1.split("-")
    #     val = str(float(n1) - float(n2))
    #
    # add_sub1_res = before + val + after
    # print("add_sub1_res", add_sub1_res, type(add_sub1_res))
    # # caculateable(new_res)
    #
    # add_sub1_res1 = re.findall("[+-]", add_sub1_res)
    # # if ("+" or "-") in add_sub1_res:
    # if add_sub1_res1:
    #     print("add_sub1_res", add_sub1_res)
    #     new_add_sub_res = add_sub(add_sub1_res)
    #     return new_add_sub_res
    # else:
    #     # r = caculateable(new_res)
    #     print("ok")
    #     # new_add_sub_res = add_sub(add_sub1_res)
    #     # return new_add_sub_res
    #     return add_sub1_res
    # # else:
    # #     return
    #     # print("add_sub")
    #     # arg = add_sub(args)
    #     # print(add_sub1)
    #     # caculateable(args)
    # #

def mut_div(args): #计算函数

    sub_formula = args
    # l2_expression = re.compile(r'(-?\d+)(\.\d+)?[/*](-?\d+)(\.\d+)?')
    # l2_expression = re.compile('-?\d+\.?\d*[*/]+-?\d+\.?\d*')
    # mut_div1 = re.search("\d+\.?\d*[*/]+-?\d+\.?\d*", sub_formula).group()
    # mut_div1 = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', args).group()

    mut_div1_check = re.search("-?\d+\.?\d*[*/]+-?\d+\.?\d*", sub_formula)
    print("mut_div1_check", mut_div1_check)

    if mut_div1_check:
        # pass
        # finished_mut_div1 = add_sub(args)
        #
        # return finished_mut_div1

        mut_div1 = re.search("-?\d+\.?\d*[*/]+-?\d+\.?\d*", sub_formula).group()
        split_formula = re.split("([*/])", mut_div1, 1)
        print("split_formula", split_formula)
        # split_formula = split_formula[0] + split_formula[1] + split_formula[2]
        # print("before", before, "after", after)
        if split_formula[1] == "*":
            val = str(float(split_formula[0]) * float(split_formula[2]))
            print("val", val)

        else:
            split_formula[1] == "/"
            # n1, n2 = mut_div1.split("/")
            val = str(float(split_formula[0]) / float(split_formula[2]))
            print("val", val)

        before, after = re.split("-?\d+\.?\d*[*/]+-?\d+\.?\d*", sub_formula, 1)
        print(before, after)
        new_formula = "%s%s%s" %(before, val, after)
        print("new_formula", new_formula)
        args = new_formula
        new_result = mut_div(args)
        return new_result
    #
    else:
        print("No")
        add_sub_res = add_sub(args)
        return add_sub_res
        # final_mut_div = mut_div(args)
        # return


# sub_mut_div_result = mut_div(new_formula)
        # return sub_mut_div_result

        # mut_div_res = before + val + after

            # print(val, type(val))
            # val = str(val)
            # print(val, type(val))
            # new_res = before + val +after
            # print(new_res, type(new_res))
        # print("mut_div_res", mut_div_res, type(mut_div_res))
        # mut_div_res1 = re.findall("[*/]", mut_div_res)
        # if mut_div_res1:
        # if ("/" or "*") in mut_div_res:
        # for i in mut_div_res:
        #     if i == "*" or "/":
                # mut_div(mut_div_res)
    #         print("new_mut_res")
    #         new_mut_res = mut_div(mut_div_res)
    #         return new_mut_res
    #     else:
    #         # r = caculateable(new_res)
    #         print("ok")
    #         add_sub_res = add_sub(mut_div_res)
    #         # caculateable(mut_div_res)
    #         return add_sub_res
    #         # return new_res
    # else:
    #     print("No")
    #     # add_sub_res = add_sub(args)
    #     # return add_sub_res
    #     # add_sub(args)


def caculateable(args):

    exp = [args, 0]
    # sub_formula = args
    # if "*" in args or "/" in args:
    # mut_div_result = mut_div(args)
    # return mut_div_result

    mut_div_result = mut_div(args)

# elif "+" in args or "-" in args:
    add_sub_result = add_sub(mut_div_result)
    print("add_sub_result", add_sub_result)
    return add_sub_result





    # final_check = re.split("[*/+-]", args)
    # if len(final_check) == 1:
    #     print("final", final_check)
    #     return final_check
    #
    # # comput_math = re.search('\d+\.?\d+[*/|+-]\d+\.?\d+', args)
    # comput_math = re.findall('[*/+-]', args)
    # print(args)
    #
    # if comput_math:
    #     if ("*" or "/") in comput_math:
    #         sub_r = mut_div(args)
    #         return sub_r
    #     # # elif "*" or "/" not in comput_math:
    #     elif ("+" or "-") in comput_math:
    #     #     # "+" or "-" in comput_math:
    #         print("add_sub")
    #         sub_r1 = add_sub(args)
    #         print("r", sub_r1)
    # return sub_r1
    # # else:
    # #     # args = caculateable(args)
    # #     return args

# origin2 = "1-2*(60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)"
origin2 = "1-2*((60-30*(9-2*5/(3+7)/3*99/4*2998+(10*568/14)))-(-4*3)/(16-3*2))"
# origin2 = "1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)"
# origin2 = "4*5-(100+2*3*50/5+100-20)*5/2+(50*2-60+100)"
# origin2 = "(100+100-100+100+100+100)"

while True:

    print(origin2)
    del_space_formula = re.sub('\s*', '', origin2)
    result = re.split("\(([^()]+)\)", del_space_formula, 1)
    print("result", result, type(result))
    if len(result) == 3:
        before, content, after = result
        sub_r = caculateable(content)
        new_str = before + str(sub_r) + after
        origin2 = new_str
    else:
        final_check = caculateable(origin2)
        print(final_check)
        break



