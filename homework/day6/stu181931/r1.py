
import re


def my_eval(strs):
    """
    计算加减乘数的函数。

    :param strs:
    :return:
    """
    temp = 0
    strs = strs.replace('--','+')
    strs = strs.replace('+-','-')
    print(strs)
    while True:
        a = re.split('(-*\d+\.*\d*[*/]-*\d+\.*\d*)',strs,1)  #使用正则表达式匹配 只包含，乘法和除法的部分
        print(a)
        if len(a) == 3:
            b = re.split('([*/])',a[1])
            if b[1] == '*':
                temp = float(b[0].strip())*float(b[2].strip())  #最内层是称号，则计算乘法
            if b[1] == '/':
                temp = float(b[0].strip())/float(b[2].strip()) #最内层是除号，则计算除法
            if a[0] == '' and a[2] == '':
                return temp
            else:
                strs = a[0].strip() + str(temp) + a[2].strip()

        else:
            a[0] = a[0].replace('--','+')  #处理掉--的符号
            a[0] = a[0].replace('+-' , '-') #处理掉+-的符号
            print(a[0])
            if '*' in a[0] or '/' in a[0]:
                d = re.split('([*/])' , a[0])
                print('ddddddddddddddddddddddd',d)
                print(d)
                if d[1] == '*':
                    temp = float(d[0].strip()) * float(d[2].strip())  # 最内层是称号，则计算乘法
                if d[1] == '/':
                    temp = float(d[0].strip()) / float(d[2].strip())  # 最内层是除号，则计算除法
            elif a[0].startswith('-'):  #如果是负号开头，添加一个0开头
                a[0] = '0'+a[0]
                c = re.split('([+-])' , a[0])   # 利用加号和减号进行字符分割
                for i in range(1 , len(c) , 2):
                    if c[i] == '+':
                        c[i + 1] = float(c[i - 1]) + float(c[i + 1])  # 进行加法运算
                    if c[i] == '-':
                        c[i + 1] = float(c[i - 1]) - float(c[i + 1]) #进行减法运算
                    temp = c[i + 1]

            else:
                c = re.split('([+-])' , a[0])
                for i in range(1,len(c),2):
                    if c[i] == '+':
                        c[i+1] = float(c[i-1]) + float(c[i+1])
                    if c[i] == '-':
                        c[i + 1] = float(c[i - 1]) - float(c[i + 1])

                    temp = c[i+1]
            return temp



def my_split(stra):
    while True:
        result = re.split('\(([^()]+)\)',stra,1)
        if len(result) == 3:
            val1 = result[0]
            val2 = result[1]
            val3 = result[2]
            stra = val1.strip() + str(my_eval(val2)) + val3.strip()
            print(stra)
        else:
            return my_eval(stra)


original = '1 - 2*( (60-30 +(-40/5) * (9-2*5/3 + 7/3*99/4*2998 +10*568/14 )) - (-4*3)/ (16-3*2) )'

t = my_split(original)
print(t)

# k = my_eval('2*3')
# print(k)

# a = re.split('(-*\d+\.*\d*[*/]-*\d+\.*\d*)' , '-40/5' , 1)
# print(a)
#
# a = re.split('(123)','123')
# print(a)