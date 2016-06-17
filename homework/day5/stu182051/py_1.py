# -*- coding:utf-8 -*-
import time
import db

def login(username, password):
    """
    用于用户名密码的验证
    :param username:用户名
    :param password:密码
    :return:Ture ，用户名验证成功，False，用户名验证失败
    """
    f = open("db", 'r', encoding='utf-8')
    for line in f:
        # 默认无参数，会移除空格符，换行符
        # 有参数：移除两侧指定的值
        line = line.strip()
        line_list = line.split("$")
        if username == line_list[0] and password == line_list[1]:
            # print("\033[35;1m登录成功\033[0m")
            return True
    return False

def register(username, password):
    """
    注册用户：
    1、打开文件a追加
    2、用户名$密码
    :param username:
    :param password:
    :return:True,注册成功
    """
    with open("db", "a", encoding='utf-8') as f:
        temp = "\n" + username + "$" + password
        f.write(temp)
        print("\033[32;1m注册用户成功\033[0m")
    return True

def user_exist(username):
    """
    检查用户名是否存在
    :param username:要检测用户名
    :return:如果用户名存在就返回True,否则False
    """
    # 去数据库一行行去查找，如果用户名存在,return True,否则False
    with open("db", 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            line_list = line.split("$")
            if line_list[0] == username:
                return True
    return False

def user_del(username,password):
    '''

    :param username: 用户名
    :param password: 密码
    :return:
    '''
    with open("db", 'r', encoding="utf-8") as f1,open("db3", 'a+', encoding="utf-8") as f2:
        for line in f1:
            if username in line:
                continue
            else:
                f2.write(line)
                print("\033[34;1m 已经成功删除用户\033[0m")

def change_pwd(username, password):
    '''

    :param username: 用户名
    :param password: 密码
    :return:
    '''
    new_pwd = input("请输入你的新密码：")
    with open("db", 'r', encoding="utf-8") as f1, open("db2", 'a+', encoding="utf-8") as f2:
        for line in f1:
            line = line.strip()
            line_list = line.split("$")
            if username in line:
                # new_pwd = input("请输入你的新密码：")
                line_list[1] = new_pwd
                f2.write(username + "$" + new_pwd + "\n")
                print("\033[34;1m密码已经重置，新密码是%s\033[0m" % new_pwd)

def shopping():
    '''

    :return:
    '''
    asset_sum = 0
    s1 = input("\033[31;1m请输入总资产:\033[0m")
    asset_sum = int(s1)

    goods = [

        {"name": "电脑", "price": 1999},

        {"name": "鼠标", "price": 50},

        {"name": "键盘", "price": 80},

        {"name": "iphone" ,"price": 5998},

    ]
    for item in goods:
        print(item["name"], item["price"])

    sp_car = {}  # 定义购物车

    while True:
        s2 = input("\033[34;1m 1:请输入商品名字,2:(Y/y结算)\033[0m")
        if s2.upper() == "Y":
            break
        for item in goods:
            if item["name"] == s2:
                name = item["name"]
                if name in sp_car.keys():
                    sp_car[name]['num'] += 1
                else:
                    sp_car[name] = {"num": 1, "unit_price": item["price"]}
    for i in range(1,2):
        print("\033[34;1m [%s %%] | [%s]\033[0m " % (int(i /1 * 100), int(i /1 * 100) * "*"))
        time.sleep(0.1)
    print("\033[31;1m 您的购物车里有以下商品\033[0m")
    print(sp_car)

    total_price = 0  # 购买所有商品的总价，初始化赋值为0

    for k, v in sp_car.items():
        u = v['unit_price']  # 购买一类商品的单价
        n1 = v['num']  # 购买一类商品的数量
        product = u * n1  # 购买一类商品的总价
        total_price += product  # 购买完所有要购买的商品的总价

    if total_price > asset_sum:
        asset_sum -= total_price
        cha = abs(asset_sum)
        print("\033[31;1m你的总资产额度不够,还差[%s]\033[0m" % cha)
        recharge = input("\033[31;1m如果你要购买现有的所有商品，请充入足够的金额:\033[0m")
        recharge_int = int(recharge)
        asset_sum += recharge_int
        print("\033[34;1m现在如果你结算，结算后余额是:[%s]\033[0m" % asset_sum)
        i1 = input("\033[31;1m如果你要继续结算请输入y,否则n:\033[0m")
        if i1 == "y":
            print("\033[34;1m购买成功，欢迎下次再来\033[0m")
    else:

        print("\033[34;1m购买成功，欢迎下次再来\033[0m")

def main():
    print("欢迎登录XXX系统")
    inp = input("\033[34;1m 1:登录；2:注册,3: 注销账号，4：重置密码，5：购物\033[0m")
    if inp == "1":
        usr = input("\033[32;1m 请输入用户名:\033[0m")
        pwd = input("\033[32;1m 请输入密码:\033[0m")
        is_login = login(usr, pwd)
        if is_login:
            print("\033[35;1m登录成功\033[0m")
        else:
            print("登录失败")
    elif inp == "2":
        usr = input("\033[32;1m 请输入用户名:\033[0m")
        pwd = input("\033[32;1m 请输入密码:\033[0m")
        is_exist = user_exist(usr)
        if is_exist:
            print("用户名已经存在，无法注册")
        else:
            register(usr, pwd)
    elif inp == "3":
        usr = input("\033[32;1m 请输入用户名:\033[0m")
        pwd = input("\033[32;1m 请输入密码:\033[0m")
        is_exist = user_exist(usr)
        if is_exist:
            user_del(usr,pwd)
            print("你输入的账号已经注销")
        else:
            print("你输入的用户不存在")
    elif inp=="4":
        usr = input("\033[32;1m 请输入用户名:\033[0m")
        pwd = input("\033[32;1m 请输入密码:\033[0m")
        is_exist = user_exist(usr)
        if is_exist:
            change_pwd(usr, pwd)
            # print("你现在的密码是%s" % new_pwd)
        else:
            print("此用户不存在")
    elif inp=="5":
        if inp == "5":
            usr = input("\033[32;1m 请输入用户名:\033[0m")
            pwd = input("\033[32;1m 请输入密码:\033[0m")
            is_login = login(usr, pwd)
            if is_login:
                print("\033[35;1m欢迎来到这里，请享受你的购物之旅\033[0m")
                shopping()
                
main()





