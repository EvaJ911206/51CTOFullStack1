from ShoppingMall import *
from LoginUser import *
from argparse import ArgumentParser

products = [
    {'name': 'pc', 'price': 1999},
    {'name': 'mouse', 'price': 10},
    {'name': 'yacht', 'price': 20},
    {'name': 'beauty', 'price': 998}
]


def show_command_after_login():
    print('%-5s%-10s' % ('id', 'command'))
    for i, cmd in enumerate(('recharge', 'show property', 'show all products',
                             'add product to cart', 'show your shopping cart',
                             'remove product from cart', 'buy! buy! buy!',
                             'Change password', 'delete user', 'show commands', 'leave')):
        print('%-5s%-10s' % (i+1, cmd))

def show_login_cmd():
    print('%-5s%-10s' % ('id', 'command'))
    for i, cmd in enumerate(('Login', 'register', 'show commands', 'leave')):
        print('%-5s%-10s' % (i + 1, cmd))

def cmd_chooser(user, logObj):
    cmd_table = {
        '1': user.add_property,
        '2': user.show_property,
        '3': user.get_product_list,
        '4': user.add_commodity,
        '5': user.show_shopping_cart,
        '6': user.rmv_commodity,
        '7': user.buy_all,
        '8': logObj.change_passwd, # What I added this time
        '9': logObj.del_user,  # What I added this time
        '10': show_command_after_login
    }
    show_command_after_login()
    while 1:
        cmd_id = input('Please input command:')
        if cmd_id in cmd_table:
            rst = cmd_table[cmd_id]()
            if rst:
                break
        else:
            if cmd_id == '11':
                print('Return to Login function')
                return
            print('Wrong command')


def user_login(logObj):
    show_login_cmd()
    cmd_table = {
        '1': logObj.login,
        '2': logObj.register,
        '3': show_login_cmd
    }
    while 1:
        cmd_id = input('Please input command:')
        if cmd_id in cmd_table:
            rst = cmd_table[cmd_id]()
            # After we login in, we can use the original
            # functions of shopping cart and change password
            if cmd_id is '1' and rst:
                if rst:
                    user = Customer(ProductList(products))
                    cmd_chooser(user, logObj)
                    show_login_cmd()
        else:
            if cmd_id == '4':
                return
            print('Wrong command')

def main(store_type):
    type_map = {
        'txt': (LoginUserContxt, ["cfg1/userConfig.txt", "cfg1/adminUserConfig.txt"]),
        'conf': (LoginUserConf, ['userInfo.conf']),
        'json': (LoginUserJson, ['userInfo.json'])
    }
    if store_type in type_map:
        user_login(type_map[store_type][0](*type_map[store_type][1]))
    else:
        print('Wrong input!')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', default='txt',
                        help='Chose the files to get and save user information;\
                    "txt" means using the txt files in folder cfg1;\
                    "conf" means using userInfo.conf\
                     "json means using userInfo.json')
    args = parser.parse_args()
    main(args.t)