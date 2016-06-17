#用户注册信息登记

import json
xx = {'alex':['123','987654321@qq.com',0]}
xx2 = {'eric':['456','123456789@qq.com',200]}
xx_str = json.dumps(xx) + '\n'
xx2_str = json.dumps(xx2) + '\n'

with open('用户信息数据库.txt','w') as reg_file:
    reg_file.writelines([xx_str,xx2_str])


with open('用户信息数据库.txt','r') as reg_file:
    for line in reg_file:
        s = line.strip()
        s_dic = json.loads(s)
        print(s_dic)

