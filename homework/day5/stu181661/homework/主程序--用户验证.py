#在登陆时，要把资产额传出来

#注册函数

def usr_dete(usr):
    '''
    用于验证注册用户的用户名是否已经已经注册过
    :param usr: 注册用户名
    :return:
    '''
    with open('用户信息数据库.txt','r') as reg_file:
        usr_list = []
        for line in reg_file:
            import json
            s = line.strip()
            s_dic = json.loads(s)
            usr_list.extend(s_dic.keys())
        if usr in usr_list:
            print('用户名已存在！请另选你的用户名！')
            return False
        else:
            print('此用户名可以注册')
            return True

def pwd_dete(pwd):
    '''
    用于限制客户注册时的密码类型
    :param pwd: 注册密码
    :return:
    '''
    ret = pwd.isalnum()
    if ret:
        print('输入的密码合法！')
        return True
    else:
        print('密码只能为数字或字母，请重新输入！')
        return False



def xx_add(usr,pwd,email,mon=0):
    '''
    用于添加用户用户注册信息
    :param usr: 注册用户名
    :param pwd: 注册密码
    :param email: 注册邮箱
    :param mon: 资产额，注册时默认为0
    :return: 注册成功
    '''
    dic = {usr:[pwd,email,mon]}
    import json
    dic_str = json.dumps(dic) + '\n'
    with open('用户信息数据库.txt','a') as reg_file:
        reg_file.write(dic_str)
    return '注册成功'

#=========================================================

#登录函数

def usr_log_dete(usr):
    '''
    用于验证登录的用户名是否存在数据库中，不在输出用户名有误
    :param usr: 登录用户名
    :return:用户存在就返回用户的个人信息
    '''
    with open('用户信息数据库.txt','r') as reg_file:
        import json
        for line in reg_file:
            s = line.strip()
            s_dic = json.loads(s)
            if list(s_dic.keys())[0] == usr:
                return s_dic
    print('你输入的用户名有误！')

def ver_code():
    '''
    生成四位有大小写字母和数字的随机验证码
    :return: 返回生成的验证码
    '''
    import random
    rad_code = ''
    for k in range(4):
        m = random.randrange(0,2)
        if m:
            n = random.randrange(0,10)
            rad_code += str(n)

        else:
            i = random.randrange(65,91)
            j = random.randrange(0,2)
            if j:
                rad_code += chr(i)
            else:
                rad_code += chr(i).lower()

    return rad_code

#====================================================================

def send_email(ema,ma):
    '''
    给邮箱发验证码
    :param ema: 要发给的邮箱
    :param ma: 验证码
    :return:
    '''
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    try:
        msg = MIMEText('密码修改验证码为%s'%ma, 'plain', 'utf-8')
        msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
        msg['To'] = formataddr(["走人",ema])
        msg['Subject'] = "淘宝账户密码修改"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("wptawy@126.com", "WW.3945.59")
        server.sendmail('wptawy@126.com', [ema,], msg.as_string())
        server.quit()
    except:
        print('发送失败！')

#==================================================================

#显示欢迎信息
print('欢迎来到淘宝网！淘！我喜欢！')

#设置账户
customer_choose = input('请选择序号来进行你接下来的操作：\n'
                        '\t1 \t登录\n'
                        '\t2 \t注册\n'
                        '\t3 \t找回密码\n'
                        '>>>')

if int(customer_choose) == 2:
    while True:
        username2 = input('请输入你要注册的用户名：')
        r1 = usr_dete(username2)
        if r1:
            break

    while True:
        passward2 = input('请输入你的注册密码：')
        r2 = pwd_dete(passward2)
        if r2:
            break

    while True:
        import re

        mailbox = input('请输入你的注册邮箱（只支持qq邮箱）：')
        m = re.findall('[0-9]{5,12}@qq\.com', mailbox)
        if m:
            print('你的注册邮箱为：', m)
            break
        else:
            print('你输入的邮箱格式有误！请重新输入！')


    r3 = xx_add(username2,passward2,mailbox)
    print(r3)

elif int(customer_choose) == 3:
    while True:
        find_usr = input('请输入要找回密码的账户名：')
        xx_dic = usr_log_dete(find_usr)
        if xx_dic:
            break


    while True:
        email1 = input('请输入你注册时的邮箱：')
        if xx_dic[list(xx_dic.keys())[0]][1] == email1:
            import random

            rand_ma = ''
            for j in range(4):
                i = random.randrange(0, 10)
                rand_ma += str(i)
            send_email(email1, rand_ma)
            break
        else:
            print('你输入的邮箱有误！请重新输入！')

    while True:
        reset = input('请输入重置验证码：')
        if rand_ma == reset:
            reset_pwd = input('请输入你重置的密码：')
            xx_dic[list(xx_dic.keys())[0]][0] = reset_pwd
            with open('用户信息数据库.txt', 'r') as reg_file:
                update_list = []
                import json

                for line in reg_file:
                    s = line.strip()
                    s_dict = json.loads(s)
                    if list(xx_dic.keys())[0] == list(s_dict.keys())[0]:
                        s_dict = xx_dic
                    s_str = json.dumps(s_dict) + '\n'
                    update_list.append(s_str)

            with open('用户信息数据库.txt', 'w') as reg_file:
                reg_file.writelines(update_list)
            print('密码修改成功！')
            break

        else:
            print('你输入的验证码错误！请重新输入！')


print('登陆页面')
while True:
    username1 = input('请输入你的用户名：')
    xx_dic = usr_log_dete(username1)
    if xx_dic:
        break

b = 1
flag = True
while flag:
    passward1 = input('请输入密码：')
    if username1 == list(xx_dic.keys())[0] and passward1 == xx_dic[list(xx_dic.keys())[0]][0]:
        print('登录成功')
        break
    else:
        print('你输入的密码有误！请重新输入！')
    b += 1
    while b > 3:
        ver_cd = ver_code()
        print('随机验证码为%s'%ver_cd)
        suijima = input('请输入随机验证码（区别大小写）:')
        if ver_cd == suijima:
            passward1 = input('请输入密码：')
            if username1 == list(xx_dic.keys())[0] and passward1 == xx_dic[list(xx_dic.keys())[0]][0]:
                print('登录成功！')
                flag = False
                break
            else:
                print('你输入的密码有误！请重新输入！')
        else:
            print('你输入的验证码错误！')



#输出账户基本信息

usermame3 = list(xx_dic.keys())[0]
money = xx_dic[list(xx_dic.keys())[0]][2]
print('亲爱的%s上帝，您当前资产为%d，'
      '你当前购物车还是空的，可以选择B开始淘宝吧！'
      '也可以选择Q退出程序！'%(usermame3,money))

customer_choose = input('请选择你的操作：')

#开始淘宝

if customer_choose.lower() == 'b':

    def recharge():
        global money
        money_num = int(input('请输入你要充值的金额：'))
        money += money_num
        print('充值成功！')
        return money


    def removes():
        re_commodity = input('请输入你要移除的商品：')
        re_choose = input('请选择你想要的操作（y-全部移除，n-移除一个）：')
        if re_choose.lower() == 'y':
            del buy_car[re_commodity]
        else:
            if buy_car[re_commodity]['数量'] != 1:
                buy_car[re_commodity]['数量'] -= 1
            else:
                del buy_car[re_commodity]
        print('移除成功！')


    import json

    with open('商品信息库.txt', 'r') as goods_file:
        goods_str = goods_file.read()
        goods_dic = json.loads(goods_str)


    def goods_father_cla():
        goods_father_list = list(goods_dic.keys())
        g_n = 0
        print('\t序号：%d \t %s \n' % (g_n + 1, goods_father_list[g_n]),
              '\t序号：%d \t %s \n' % (g_n + 2, goods_father_list[g_n + 1]),
              '\t序号：%d \t %s \n' % (g_n + 3, goods_father_list[g_n + 2]))
        choose_num = int(input('请选择要淘宝品类的序号:')) % 3
        return [choose_num, goods_father_list]


    def goods_son_cla(father_cla):
        goods_son_list = list(goods_dic[father_cla].keys())
        g_n = 0
        print('\t序号：%d \t %s \n' % (g_n + 1, goods_son_list[g_n]),
              '\t序号：%d \t %s \n' % (g_n + 2, goods_son_list[g_n + 1]))
        choose_num = int(input('请选择要淘宝品类的序号:')) % 2
        return [choose_num, goods_son_list]


    def baobei(father_cla, son_cla):
        baobei_list = list(goods_dic[father_cla][son_cla].keys())
        g_n = 0
        print('\t序号：%d \t 商品名：%s \t价格：%s\n'
              % (g_n + 1, baobei_list[g_n], goods_dic[father_cla][son_cla][baobei_list[g_n]]),
              '\t序号：%d \t 商品名：%s \t价格：%s\n'
              % (g_n + 2, baobei_list[g_n + 1], goods_dic[father_cla][son_cla][baobei_list[g_n + 1]]))
        choose_num = int(input('请选择要添加到购物车宝贝的序号:')) % 2
        baobei_num = input('请输入你要购买宝贝的数量（不输默认为1）：')
        if choose_num == 1:
            buy_car[baobei_list[g_n]] = {}
            buy_car[baobei_list[g_n]]['价格'] = goods_dic[father_cla][son_cla][baobei_list[g_n]]
            if baobei_num == '':
                buy_car[baobei_list[g_n]]['数量'] = 1
            else:
                buy_car[baobei_list[g_n]]['数量'] = int(baobei_num)
        else:
            buy_car[baobei_list[g_n + 1]] = {}
            buy_car[baobei_list[g_n + 1]]['价格'] = goods_dic[father_cla][son_cla][baobei_list[g_n + 1]]
            if baobei_num == '':
                buy_car[baobei_list[g_n + 1]]['数量'] = 1
            else:
                buy_car[baobei_list[g_n + 1]]['数量'] = int(baobei_num)


    print('亲！开始淘宝了！')
    buy_car = {}
    # {商品：{价格：xx，数量：xx}}

    while True:
        choose_list_f = goods_father_cla()
        fa_cla = choose_list_f[1][choose_list_f[0] - 1]
        choose_list_s = goods_son_cla(fa_cla)
        so_cla = choose_list_s[1][choose_list_s[0] - 1]
        choose_list_b = baobei(fa_cla, so_cla)
        c_choose = input('选择y进入结算，选择q退成程序，不填则继续淘宝:')
        if c_choose.lower() == 'y':
            break
        elif c_choose.lower() == 'q':
            exit()
        else:
            continue

    print('你的购物车：', buy_car)

    # 计算交易额
    turnover = 0
    for k in buy_car:
        turnover += buy_car[k]['价格'] * buy_car[k]['数量']
    print('此笔交易额为：', turnover)

    # 结算
    if turnover > money:
        print('你当前余额不足！')
        print('你此次交易还差%d' % (turnover - money))
        c_choose = input('你可选择r移除商品，选择c充值，选择q退出程序：')
        if c_choose.lower() == 'r':
            print('你的购物车：', buy_car)
            removes()
            print('交易成功！')
        elif c_choose.lower() == 'c':
            money = recharge()
            print('交易成功！')
        elif c_choose.lower() == 'q':
            exit()
    else:
        print('交易成功！')
        print('交易后你的资产额为%d' % (2000 - turnover))


elif customer_choose.lower() == 'q':
    print('正在退出当前程序！')
    exit()

#========================================================================================
#选择邮寄地址

import json
with open('地区信息库.txt','r') as area_file:
    area_str = area_file.read()
    area_dict = json.loads(area_str)



def city(area_sources):
    list_p = []    #用来存储信息的列表['江西','湖南','浙江']
    for area in area_sources:
        list_p.append(area)
    p_n = 0       #序号变量，也可以用于列表索引
    print('\t序号：%d \t地区：%s \n'%(p_n,list_p[p_n]),    #输出信息页面
          '\t序号：%d \t地区：%s \n'%(p_n + 1, list_p[p_n + 1]),
          '\t序号：%d \t地区：%s \n'%(p_n + 2, list_p[p_n + 2]))
    choose_num = input('请选择你要寄往的区号：')             #选择地区序号
    return [int(choose_num),list_p]   #[1,['江西','湖南','浙江']]

print('韵达快递为你服务！')
choose_list = city(area_dict)
if choose_list[0] == 0:
    youji_province = choose_list[1][choose_list[0]]
    area_s = area_dict[youji_province]
    choose_list = city(area_s)

    if choose_list[0] == 0:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s'%(youji_province,youji_city,youji_county))

    elif choose_list[0] == 1:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s'%(youji_province,youji_city,youji_county))

    elif choose_list[0] == 2:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s'%(youji_province,youji_city,youji_county))
    else:
        pass


elif choose_list[0] == 1:
    youji_province = choose_list[1][choose_list[0]]
    area_s = area_dict[youji_province]
    choose_list = city(area_s)

    if choose_list[0] == 0:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))

    elif choose_list[0] == 1:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))

    elif choose_list[0] == 2:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))
    else:
        pass

elif choose_list[0] == 2:
    youji_province = choose_list[1][choose_list[0]]
    area_s = area_dict[youji_province]
    choose_list = city(area_s)

    if choose_list[0] == 0:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))

    elif choose_list[0] == 1:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))

    elif choose_list[0] == 2:
        youji_city = choose_list[1][choose_list[0]]
        area_s = area_dict[youji_province][youji_city]
        choose_list = city(area_s)
        youji_county = choose_list[1][choose_list[0]]
        print('你寄往的地址为--%s%s%s' % (youji_province, youji_city, youji_county))
    else:
        pass

else:
    pass

print('宝贝正飞速飞向你的家中，请耐心等待！')










