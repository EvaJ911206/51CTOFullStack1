#!/usr/bin/env python
#_*_codng:utf-8_*_


def login(username,password):
    """
    用户名和密码的验证函数
    :param username:snow123
    :param password:123
    :return:注册成功返回True
    """
    f = open("pwd",'r',encoding='utf-8')
    for i in f:
        i = i.strip()
        i_list = i.split("*")
        if username == i_list[0] and password == i_list[1]:
            return True
    return False

def zhuce(username,password):
    """
    用于用户的注册函数
    :param username:snowman
    :param password:123
    :return:注册成功返回True
    """
    with open("pwd","a",encoding="utf-8") as f:
        temp = "\n" + username + "*" + password
        f.write(temp)
    return True


def shanchu(usershanchu):
    """
    用于用户删除指定的用户
    :param usershanchu:传入参数为需要删除的用户名参
    :return: 删除成功返回True
    """
    import re
    #usershanchu = input("请输入要删除的用户名：")
    lines = []
    f = open("pwd", "r", encoding="utf-8")
    for line in f.readlines():
        if not re.search(usershanchu, line):
            lines.append(line)
            return False
    f.close()


    f = open("pwd", "w", encoding="utf-8")
    f.writelines(lines)
    f.close()
    return True

def xiugai(pwd2,pwd3):
    """
    用于用户修改密码的函数
    :param pwd2: 该传入参数为用户原密码
    :param pwd3: 该传入参数为用户新密码
    :return: 修改成功返回True
    """
    #pwd2 = input("请输入新密码：")
    ff = open("pwd", "r+", encoding="utf-8")

    for s in ff.readlines():
        ff.write(s.replace(pwd2, pwd3))

    ff.close()
    return True

def user_exist(username):
    """
    用于系统检测是否存在同名用户名
    :param username: 该传入参数为用户输入的用户名
    :return: 如果存在返回False
    """
    with open("pwd",'r',encoding="utf-8") as f:
        for i in f:
            i = i.strip()
            i_list = i.split("*")
            if i_list[0] == username:
                return True
    return False

def shop():
    """
    该函数为购物的主函数，在用户登陆成功后调用该函数
    :return:
    """
    asset_all = 0

    i1 = input("请输入总资产:")
    asset_all = int(i1)

    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]

    for i in goods:
        print(i['name'], i['price'])
    car_dict = {}
    while True:
        i2 = input("请选择商品(Y/y结算)：")
        if i2.lower() == "y":
            break
        for item in goods:
            if item['name'] == i2:
                name = item['name']
                if name in car_dict.keys():
                    car_dict[name]['num'] = car_dict[name]['num'] + 1
                else:
                    car_dict[name] = {"num": 1,"single_price":item['price']}
    print(car_dict)
    all_price = 0
    for k,v in car_dict.items():
        n = v['singe_price']
        m = v['num']
        all_sum = m * n
        all_price = all_price + all_sum

    if all_price > asset_all:
        print("没钱")
    else:
        print("我是主人的")

def main():
    """
    购物车的主程序，用于调用其他函数和子程序
    :return:
    """
    print("""
        *********************************************************************
                               欢迎来到雪国购物车
        # 登录请按“1”，注册请按“2”，删除用户请按“3”，修改密码请按“4”#
        *********************************************************************
    """)
    inp = input("1.登陆: 2.注册： 3.删除用户： 4.修改密码: ")

    user = input("请输入用户：")
    pwd = input("请输入密码：")
    if inp == "1":

        i_login = login(user,pwd)
        if i_login:
            print("登陆成功")
            shop()
        else:
            print("登陆失败")
    elif inp == "2":
        i_exist = user_exist(user)
        if i_exist:
            print("用户名已经存在，不能注册")
        else:
            result = zhuce(user,pwd)
            if result:
                print("注册成功")
            else:
                print("注册失败")
    elif inp == "3":
        usershanchu = input("请输入要删除的用户名：")
        i_shanchu = shanchu(usershanchu)
        if i_shanchu:
            print("删除用户成功")
        else:
            print("删除用户失败")
    elif inp == "4":
        pwd2 = input("请输入原密码：")
        pwd3 = input("请输入新密码：")
        i_xiugai = xiugai(pwd2,pwd3)
        if i_xiugai:
            print("修改密码成功")
        else:
            print("修改密码失败")

main()
