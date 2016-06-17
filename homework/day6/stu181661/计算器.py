#题目：求得字符串里'1-2*((60-30+9*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'计算式的结果


import re

#匹配规则
brackets = re.compile('\(([^()]+)\)')
powers = re.compile('(\d+\.?\d*)\*\*(\-?\d+\.?\d*)')
mul_div = re.compile('(\-?\d+\.?\d*)([*/])(\-?\d+\.?\d*)')
add_cut = re.compile('(\-?\d+\.?\d*)([+\-])(\-?\d+\.?\d*)')

def powers_calculate(match_obj):
    '''
    处理幂运算
    :param match_obj: 需要处理的match对象
    :return:算式的结果
    '''
    mat_grs = match_obj.groups()
    n1 = float(mat_grs[0])
    n2 = float(mat_grs[1])
    return n1**n2

def mul_div_calculate(match_obj):
    '''
    处理乘除运算
    :param match_obj: 需要处理的match对象
    :return: 算式的结果
    '''
    mat_grs = match_obj.groups()
    n1 = float(mat_grs[0])
    n2 = float(mat_grs[2])
    if mat_grs[1] == '*':
        return n1*n2
    else:
        return n1/n2

def add_cut_calculate(match_obj):
    '''
    处理加减运算
    :param match_obj: 需要处理的match对象
    :return: 算式的结果
    '''
    mat_grs = match_obj.groups()
    n1 = float(mat_grs[0])
    n2 = float(mat_grs[2])
    if mat_grs[1] == '+':
        return n1+n2
    else:
        return n1-n2


#数据源
data_sour = '1-2*((60-30+9*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

# data_sour = input('请输入你要计算的算式：')
#==================================================================================

#匹配最底层的括号
brackets_match = brackets.search(data_sour)

#对匹配到的括号进行处理
while True:
    if brackets_match:                  #判断匹配成功与否
        print(brackets_match.group())   #(9-2*5/3+7/3*99/4*2998+10*568/14)
        mat_groups1 = brackets_match.groups()  #得到去括号的组的值，不过此时这里是元组
        print(mat_groups1)              #('9-2*5/3+7/3*99/4*2998+10*568/14',)

        #处理幂运算
        text = mat_groups1[0]      #得到最底层括号里的算式字符串
        powers_match = powers.search(text)  #匹配幂运算
        while True:
            if powers_match:                #判断匹配成功与否
                print(powers_match.group())
                ret1 = powers_calculate(powers_match) #调用幂运算函数
                print(ret1)
                text = re.sub(powers,str(ret1),text,1)  #把得到的幂运算结果替换匹配到的字符串
                powers_match = powers.search(text)      #对替换的字符串再次进行幂运算匹配
            else:
                break                        #匹配失败，就退出匹配幂运算的循环

        #处理乘除运算
        mul_div_match = mul_div.search(text)  #对处理幂运算后的字符串进行乘除运算匹配
        while True:
            if mul_div_match:                 #判断匹配成功与否
                print(mul_div_match.group())
                ret2 = mul_div_calculate(mul_div_match)  #调用乘除运算函数
                print(ret2)
                text = re.sub(mul_div,str(ret2),text,1)  #把得到的乘除运算结果替换匹配的字符串
                print(text)
                mul_div_match = mul_div.search(text)     #对处理后的字符串再进行乘除运算匹配
            else:
                break   #匹配失败，就退出匹配乘除运算的循环

        #处理加减运算
        add_cut_match = add_cut.search(text)    #对处理乘除后的字符串进行加减运算匹配
        while True:
            if add_cut_match:                   #判断匹配成功与否
                print(add_cut_match.group())
                ret3 = add_cut_calculate(add_cut_match)  #调用加减运算函数
                text = re.sub(add_cut,str(ret3),text,1)  #用得到的加减运算结果替换匹配的字符串
                print(text)
                add_cut_match = add_cut.search(text)  #对处理后的字符串再进行加减运算匹配
            else:
                break      #匹配失败，退出匹配加减运算的循环

        data_sour = re.sub(brackets,text,data_sour,1)  #把括号里的计算结果替换匹配的括号
        brackets_match = brackets.search(data_sour)   #再次对处理后字符串进行括号的匹配

    else:
        break     #匹配不到括号，就退出匹配括号的循环

#对处理括号完后的算式进行最后的运算
#幂
powers_match = powers.search(data_sour)
while True:
    if powers_match:
        ret1 = powers_calculate(powers_match)
        data_sour = re.sub(powers,str(ret1),data_sour,1)
        powers_match = powers.search(data_sour)
    else:
        break

#乘除
mul_div_match = mul_div.search(data_sour)
while True:
    if mul_div_match:
        ret1 = mul_div_calculate(mul_div_match)
        data_sour = re.sub(mul_div, str(ret1), data_sour, 1)
        mul_div_match = mul_div.search(data_sour)
    else:
        break

#加减
add_cut_match = add_cut.search(data_sour)
while True:
    if add_cut_match:
        ret1 = add_cut_calculate(add_cut_match)
        data_sour = re.sub(add_cut, str(ret1), data_sour, 1)
        add_cut_match = add_cut.search(data_sour)
    else:
        break

print('最后结果为：',data_sour)

#验证结果
data_sour = '1-2*((60-30+9*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
jieguo = eval(data_sour)
print('验证结果：',jieguo)
















