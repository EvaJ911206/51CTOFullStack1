# !/usr/bin/python

global USERDICT
global LOGINUSERDICT


# 错误提示
ERROR = [
    "登录成功",
    "用户名不存在",
    "密码错误",
    "注册成功",
    "用户名为以下划线或字母开头的6~16位字符",
    "密码为以下划线或字母开头的6~16位字符",
    "两次输入密码不一致",
    "密码修改成功",
    "只有使用管理员账户登录，才可进行删除用户操作！",
    "用户名已存在",
    "删除用户操作成功",
    "不能对管理员用户进行删除操作"
]

import re

# 用户名及密码命名规则
parrten = re.compile("^[a-zA-Z_]\w{5,15}$")


# def islogin(func):
#     def inner(*args):
#         if args[0] in LOGINUSERDICT.keys:
#             func()
#     return inner


# 装饰器，判断是否是管理员用户
def isadmin(func):
    def inner():
        if "admin" in LOGINUSERDICT.keys():
            re = func()
            return re
        else:
            flag = 8
            return flag
    return inner


# 登录
def login():
    flag = 0
    name = input("请输入用户名：")
    if name in USERDICT.keys():
        pwd = input("请输入密码：")
        if USERDICT[name] == pwd:
            LOGINUSERDICT.clear()
            LOGINUSERDICT[name] = pwd
            print("欢迎 %s 登录成功" % name)
        else:
            flag = 2
    else:
        flag = 1
    return flag


# 注册
def register():
    flag = 3
    name = input("请输入用户名：").strip()
    n_match = parrten.match(name)
    if n_match is None:
        flag = 4
    elif name in USERDICT.keys():
        flag = 9
    else:
        pwd = input("请输入密码：").strip()
        p_match = parrten.match(pwd)
        if p_match is None:
            flag = 5
        else:
            tpwd = input("请确认密码：").strip()
            if pwd == tpwd:
                USERDICT[name] = pwd
                LOGINUSERDICT.clear()
                LOGINUSERDICT[name] = pwd
                with open("userinfo", "a+", encoding="utf-8") as f:
                    f.write("%s=%s" % (name, pwd))
            else:
                flag = 6
    return flag


# 修改密码
def chgpwd():
    flag = 7
    name = input("请输入用户名：")
    if name in USERDICT.keys():
        pwd = input("请输入原密码：")
        if USERDICT[name] == pwd:
            npwd = input("请输入新密码：")
            renpwd = input("请确认密码：")
            if npwd.strip() == renpwd.strip():
                USERDICT[name] = npwd
                with open("userinfo", "w+", encoding="utf-8") as f:
                    for k in USERDICT.keys():
                        f.write("%s=%s\n" % (k, USERDICT[k]))
            else:
                flag = 6
        else:
            flag = 2
    else:
        flag = 1
    return flag


# 管理员身份删除用户
@isadmin
def deluser():
    flag = 10
    name = input("请输入用户名：").strip()
    # 输入用户名存在于USERDICT且不等于admin，不能进行删除admin管理员操作
    if name in USERDICT.keys():
        if name == "admin":
            flag = 11
        else:
            USERDICT.pop(name)
            with open("userinfo", "w+", encoding="utf-8") as f:
                for k in USERDICT.keys():
                    f.write("%s=%s\n" % (k, USERDICT[k]))
    else:
        flag = 1
    return flag

# 选择操作使用的函数
def oper(no):
    re = index.get(no)()
    return re

# 命令序号对应的操作函数
index = {"1": login, "2": register, "3": chgpwd, "4": deluser}
# 命令菜单
menu = ["登录", "注册", "修改密码", "删除用户"]
# 用来存储用户密码配置文件内容的dict
USERDICT = dict()
# 用来存储当前登录用户的dict
LOGINUSERDICT = dict()


# 主函数
if __name__ == "__main__":
    # 打开配置文件，并将内容读入到USERDICT中
    with open("userinfo", "r") as f:
        for line in f:
            user = line.split("=")
            USERDICT[user[0]] = user[1].split("\n")[0]
    while True:
        print("%4s\t%8s" % ("序号", "操作"))
        for m in enumerate(menu):
            print("%4s\t%8s" % (m[0]+1, m[1]))
        print()
        no = input("请输入：")
        if no.isdigit():
            re = oper(no)
            print(ERROR[re])
            continue
        elif no.strip().lower() == "q":
            print("程序退出~~~")
            break
