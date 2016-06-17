#!/usr/bin/env python3
#_*_coding:utf-8_*_
import re


def exec(calcu_list):
    """
    去除括号函数
    :param calcu_list:
    :return: 最后计算结果
    """
    #匹配最里层的括号，(-40.0/5)
    #如果没有匹配到，直接返回表达式
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', calcu_list[0]):
        final = compute(calcu_list[0])
        calcu_list[0] = final
        return calcu_list
    #正则表达式取到最里面的括号的内容，而且去掉两边的括号，得到content
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', calcu_list[0]).group()
    #按匹配的内容进行分割，得到before匹配的内容，而after得到两边的内容
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', calcu_list[0], 1)
    print ('before：', calcu_list)
    #只取字符串中第1个和倒数第2个的内容，去掉两侧的括号
    content = content[1:len(content) - 1]
    #将得到的content进行计算，得到结果
    ret = compute(content)
    print ('%s=%s' % (content, ret))
    calcu_list[0] = "%s%s%s" % (before, ret, after)
    print ('after：', calcu_list)
    print ("#" * 20, '上一次计算结束', "#" * 20)
    #递归执行exec
    exec(calcu_list)

def compute(expr):
    """
    计算加减乘除函数
    :param expr:
    :return: 计算结果
    """
    #将表达式放在calcu列表中，
    calcu = [expr, 0]
    #先进行乘除运算
    compute_intend(calcu)
    #再进行加减运算
    compute_add(calcu)
    #判断calcu[1]是奇数还是偶数，若为奇数，结果为负数，否则为正数
    if divmod(calcu[1], 2)[1] == 1:
        result = float(calcu[0])
        result = result * -1
    else:
        result = float(calcu[0])
    return result

def compute_intend(arg):
    """
    计算乘除函数
    :param arg:
    :return: 计算结果
    """
    value = arg[0]
    #对字符串进行乘除匹配
    rule = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', value)
    #没有匹配到直接返回结果
    if not rule:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', value).group()
    #对匹配的结果进行乘除判断，然后计算
    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        get_value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        get_value = float(n1) / float(n2)
    #取出两头的内容
    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', value, 1)
    #拼接型的字符串
    new_str = "%s%s%s" % (before, get_value, after)
    arg[0] = new_str
    #再次进行递归处理
    compute_intend(arg)

def compute_add(arg):
    """
    计算加减函数
    :param arg:
    :return: 计算结果
    """
    #将表达式中的++、--变成+，+-、-+变成-，处理完成退出
    while True:
        if arg[0].__contains__('--') or arg[0].__contains__('+-') or arg[0].__contains__('--') or arg[0].__contains__(
                '-+'):
            arg[0] = arg[0].replace('--', '+')
            arg[0] = arg[0].replace('+-', '-')
            arg[0] = arg[0].replace('-+', '-')
            arg[0] = arg[0].replace('--', '+')
        else:
            break
    #对字符串二次处理，提取首位为’-‘，保存在arg[1]中
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-', '&')
        arg[0] = arg[0].replace('+', '-')
        arg[0] = arg[0].replace('&', '+')
        arg[0] = arg[0][1:]
    value = arg[0]
    #对字符串value进行匹配，匹配加减的内容
    rule = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', value)
    #没有匹配到直接返回
    if not rule:
        return
    #将匹配的内容保存在content中
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', value).group()
    #对匹配的内容进行判断计算
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        get_value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        get_value = float(n1) - float(n2)
    #取出匹配内容两头的内容，放在before和after中
    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', value, 1)
    new_str = "%s%s%s" % (before, get_value, after)
    arg[0] = new_str
    #进行递归计算
    compute_add(arg)

if __name__ == "__main__":
    print ('#' * 10, "计算表达式：", "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )", '#' * 10)
    str = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
    #去掉表达式中的空格
    str = re.sub('\s*', '', str)
    calcu_list = [str, ]
    #执行去括号处理函数，并计算最终结果
    exec(calcu_list)
    ret = calcu_list[0]
    #打印最终计算结果
    print ("我的计算结果：", ret)
