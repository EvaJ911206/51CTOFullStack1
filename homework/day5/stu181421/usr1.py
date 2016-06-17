#!/usr/bin/python3
# coding=utf-8
__author__ = 'jizas'
"""
实现一个系统，提供登录界面，并有老用户登录，新用户注册（支持检查用户是否存在），修改用户密码，注销用户等功能
"""


def loadinf(usr, pwd):
    with open('SAM', 'r') as f:
        for i in f:
            u1 = i.split('@@')[0]
            p1 = i.split('@@')[1].strip()
            if usr == u1 and pwd == p1:
                return 1
            else:
                continue
    return 0


def ext(usr):
    try:
        with open('SAM', 'r') as f:
            for i in f:
                if usr == i.split('@@')[0]:
                    print("用户名已存在！")
                    return 0
                else:
                    continue
            return 1
    except:
        print("文件不存在!")


def addinf(usr, pwd):
    with open('SAM', 'a') as f:
        f.write(usr + "@@" + pwd + '\n')
        print("注册成功!")


def modinf(usr):
    npwd = input("请输入新密码:")
    with open('SAM', 'r') as f:
        data = f.readlines()
#        len1 = len(data) - 1
        for i in range(len(data)):
            if usr == data[i].split('@@')[0]:
                data[i] = data[i].replace(data[i].strip(), usr + '@@' + npwd)
    with open('SAM', 'w') as f:
        f.writelines(data)


def login(usr, pwd):
    if loadinf(usr, pwd):
        print("登录成功")
        return True
    else:
        print("登录失败！请检查用户名与密码是否正确")
        return False


def reg():
    usr = input("请输入用户名：")
    pwd = input("请输入密码：")
    if ext(usr):
        addinf(usr, pwd)
        return 1
    else:
        return 0


def unreg(usr):
    comf = input("您确认不再使用本用户了吗?是则选y:")
    if comf == 'y':
        with open('SAM', 'r') as f:
            data = f.readlines()
            for i in range(len(data)):
                if usr == data[i].split('@@')[0]:
                    data[i] = data[i].replace(data[i], '')
        with open('SAM', 'w') as f:
            f.writelines(data)
        return 1
    else:
        print("您的输入有误")
        return 0


def usrmain():
    while True:
        dint = input("欢迎光临本系统!\n1.用户登录\n2.用户注册\n3.退出\n请输入序号：")
        if dint == '1':
            usr = input("请输入用户名：")
            pwd = input("请输入密码：")
            if login(usr, pwd):
                while True:
                    qint = input("欢迎回来!\n1.密码修改\n2.注销\n3.退出\n请输入序号：")
                    if qint == '1':
                        modinf(usr)
                    elif qint == '2':
                        if unreg(usr):
                            break
                        else:
                            continue
                    else:
                        break
        elif dint == '2':
            reg()
        elif dint == '3':
            print("再见")
            return 0
        else:
            print("您的输入有误！请重新输入")


if __name__ == '__main__':
    usrmain()
