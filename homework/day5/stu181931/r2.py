#!/usr/bin/evn python
#-*- coding:utf-8 -*-


def getuser():
    """
    得到用户名
    :return: 返回用户名
    """
    user = input('请输入用户名：')
    return user


def getpwd():
    """
    得到密码
    :return: 返回密码
    """
    pwd = input('请输入密码：')
    return pwd


def login(user,pwd):
    """
    用来验证用户和密码
    :param user: 用户名
    :param pwd: 密码
    :return: 登录成功返回True，失败False
    """
    with open('data','r') as f1:
        for line in f1:
            line = line.strip() #截取前后空格
            li = line.split('&')
            if user == li[0] and pwd == li[1]: #验证登陆
                return True
        return False


def exists(user):
    """
    判断用户是否存在
    :param user: 用户名
    :return: 密码
    """
    with open('data','r') as f2:
        for line in f2:
            line = line.strip()
            li = line.split('&')
            if user == li[0]:
                return True
    return False


def register(user,pwd):
    """
    添加账号和密码
    :param user: 用户名
    :param pwd: 密码
    :return:
    """
    with open('data','a') as f3:
        newuser = '\n'+ user+'&'+pwd
        f3.write(newuser)

# def defuser(user):
#     """
#     删除用户
#     :param user: 用户名称
#     :return: 删除成功返回True，删除失败返回False
#     """
#     with open('data','r+') as f4:
#         for line in f4:
#             li = line.strip().split('&')
#             if li[0] == user:
#                 a = f4.tell()
#                 l = len(line)
#                 f4.seek(a - l)  # 回到行首指针
#                 f4.write('****del_user****')# 删除用户名称，将用户明修改为****del_user****
#                 return True
#     return False


def deluser(user):
    """
    删除用户
    :param user: 用户名称
    :return: 删除成功返回True，删除失败返回False
    """
    with open('data','r+') as f4:
        li = f4.readlines() # 将文件读取到列表中
        for line in li:
            li2 = line.strip().split('&')
            if li2[0] == user:
                li.remove(line) #列表删除用户
                f4.truncate(0)
                f4.seek(0)
                for newline in li:
                    f4.write(newline)
                return True
    return False


def updateuser(user,pwd):
    """
    更新用户密码
    :param user: 用户名称
    :return: 更新成功返回True，更新失败返回False
    """
    newpwd = input('请输入新的密码: ')
    with open('data','r+') as f4:
        li = f4.readlines() # 将文件读取到列表中
        for i in range(len(li)):
            li2 = li[i].strip().split('&')
            if li2[0] == user and li2[1] == pwd:
                li[i] = (user + '&' + newpwd + '\n')
                f4.truncate(0)
                f4.seek(0)
                for newline in li:
                    f4.write(newline)
                return True
    return False


def main():
    """
    main 函数，接受用户的输入，根据数据执行对应的函数
    :return:
    """
    print('欢迎登陆测试系统，请选择操作：')
    while True:
        inp = input('1: 登录；2：注册；3：退出系统\n')
        if inp == '1':
            user = getuser()
            pwd = getpwd()
            t = login(user,pwd)
            if t:
                print('登录成功')
                if user == 'admin':
                    while(True):
                        inp2 = input('1: 修改密码；2：删除用户；3: 返回\n')  #如果登陆账号是amdin，打印删除用户和修改密码菜单
                        if inp2 == '1':
                            result = updateuser(user,pwd)
                            if result:
                                print('修改成功')
                            else:
                                print('修改失败')
                        elif inp2 =='2':
                            inpuser = input('请输入要删除的账号：')
                            if exists(inpuser) and inpuser != user:
                                result2 = deluser(inpuser)
                                if result2:
                                    print('删除成功')
                                else:
                                    print('删除失败')
                            else:
                                print('用户不存在')
                        elif inp2 == '3':
                            break
                        else:
                            print('输入错误！')
                else:
                    while (True):
                        inp3 = input('1: 修改密码；2: 返回\n')  # 如果登陆账号不是amdin，不打印删除用户和修改密码菜单
                        if inp3 == '1':
                            result = updateuser(user , pwd)
                            if result:
                                print('修改成功')
                            else:
                                print('修改失败')
                        elif inp3 == '2':
                            break
                        else:
                            print('输入错误！')
            else:
                print('登录失败')
        elif inp == '2':
            user = getuser()
            t = exists(user)
            if t:
                print('用户名已经存在，无法注册')
            else:
                pwd = getpwd()
                register(user,pwd)
                print('注册成功')
        elif inp == '3':
            break
        else:
            print('输入错误！， 请重新输入')



main()
