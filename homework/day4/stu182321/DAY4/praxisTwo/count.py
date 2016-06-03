#!/usr/bin/env python
# coding:utf-8
# 写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数


def count_str(arg):
    """
    :param arg: str
    :return: None
    """
    nums, letters, blanks, others = 0, 0, 0, 0
    for item in arg:
        if item.isdigit():
            nums += 1
        elif item.encode('utf-8').isalpha():
            letters += 1  # 中文也会被认为是一个字母
        elif item.isspace():
            blanks += 1
        else:
            others += 1
    print("字符串%s中有数字%d个，字母%d个，空格%d个以及其他字符%d个。" % (arg, nums, letters, blanks, others))

ret = "你好Hello Old2222boy Python study!"
count_str(ret)
