import re
val="1-2*((60-30*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
def chen(arg):
    f = arg
#    print (f)
    if "*" in arg or "/" in arg:
        '''如果包含*号或者除好则进如该方法'''
        b2_2 = re.search("\d+\.?\d*[*/]+-?\d+\.?\d*", arg)
        m = b2_2.group()
        k = re.split("([*/])", m, 1)
        kn = k[0] + '\\' + k[1] + k[2]
        if k[1] == '*':
           new_a = float(k[0]) * float(k[2])
           f = re.sub(kn, str(new_a), arg)
           new_z = chen(f)
           return new_z
        elif k[1] == '/':
           new_a = float(k[0]) / float(k[2])
           f = re.sub(kn, str(new_a), arg)
           new_z = chen(f)
           return new_z
    elif re.match("-+\d+\.?\d*[+-]+\d+\.?\d*",arg):
        '''如果是负数的减法则进如该方法'''
        m = re.search("-+\d+\.?\d*[+-]+\d+\.?\d*", arg).group()
        k = re.split("([+-])", m, 1)
        kt =re.split("([+-])", m, 2)
        kn = k[0] + '\\' + k[1] + k[2]
        aa = "%s%s" %(kt[1],kt[2])
        if kt[3] == '-':
            new_a = float(aa) - float(kt[4])
            f = re.sub(kn, str(new_a), arg)
            new_z = chen(f)
            return new_z
    elif re.search("\d+\.?\d*[+-]+\d+\.?\d*", arg):
        '''如果是 加号和减号则进如该方法'''
#        b2_2 = re.search("\d+\.*\d*[+-]+\d+\.*\d*", arg)
        b2_2 = re.search("\d+\.?\d*[+-]+\d+\.?\d*", arg)
        m = b2_2.group()
        k = re.split("([+-])", m, 1)
        kn = k[0] + '\\' + k[1] + k[2]
       # print (k)
        if k[1] == '+':
            new_a = float(k[0]) + float(k[2])
            f = re.sub(kn, str(new_a), arg)
            new_z = chen(f)
            return new_z
        elif k[1] == '-':
            new_a = float(k[0]) - float(k[2])
            f = re.sub(kn, str(new_a), arg)
            new_z = chen(f)
            return new_z
    return f

#b = re.split("\(([^()]+)\)",val,1)
while True:
    b = re.split("\(([^()]+)\)", val, 1)
    if len(b) == 3:
    #    print (b)
        a1,a2,a3=b
        chen1=chen(a2)
        val = "%s%s%s" %(a1,chen1,a3)
    else:
        val=chen(val)
        print (val)
        break