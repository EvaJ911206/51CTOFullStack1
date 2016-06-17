# !/usr/bin/python
import re
def mul(args):
    if "**" in args:
        a = re.search("-?\d+\.?\d*\*{2}-?\d+\.?\d*", args)
        k = re.split("(\*{2})", a.group(), 1)
        kn = k[0]+"\\*\\*"+k[2]
        new_a = float(k[0])**float(k[2])
    elif "*" in args or "/" in args:
        a = re.search("\d+\.?\d*[*/]-?\d+\.?\d*", args)
        k = re.split("([*/])", a.group(), 1)
        kn = k[0]+"\\"+k[1]+k[2]
        if k[1] == "*":
            new_a = float(k[0])*float(k[2])
        elif k[1] == "/":
            new_a = float(k[0])/float(k[2])
    else:
        flag = 1
        arg = ""
        temp = args
        if args[0] == "-":
            temp = args[1:]
            flag = -1
            arg = "-"
        a = re.search("-?\d+\.?\d*[+-]+-?\d+\.?\d*", temp)
        k = re.split("([+-])", a.group(), 1)
        kn = arg+k[0]+"\\"+k[1]+k[2]
        if k[1] == "+":
            new_a = flag*float(k[0])+float(k[2])
        elif k[1] == "-":
            new_a = flag*float(k[0])-float(k[2])
    f = re.sub(kn, str(new_a), args)
    if re.search("-?\d+\.?\d*[+\-/*]+", f):
        new_z = mul(f)
    else:
        new_z = f
    return new_z
def calculate(args):
    while True:
        n = re.findall(r"\(([^()]+)\)", args)
        if len(n):
            for i in n:
                result = mul(i)
                new_str = args.replace("("+i+")", result)
                args = new_str
        else:
            args = mul(args)
            break
    return args
if __name__ == "__main__":
    origin = "1 - 2 * ((60 - 30 + (-40.0 / 5) * (9 - 1 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 ** 3) / (16 - 3 * 2))"
    s = re.sub("\s", "", origin)
    result = calculate(s)
    print("该表达式计算结果为："+result)

