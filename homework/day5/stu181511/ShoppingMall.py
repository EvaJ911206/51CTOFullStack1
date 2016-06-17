

class NumChecker(object):
    def __init__(self, start=0, end=None):
        self.start = start
        self.end = end

    @staticmethod
    def is_int(chk_num):
        # In my opinion, using int to try is batter than isdigit
        try:
            chk_num = int(chk_num)
        except Exception as e:
            print("Please input number not other character. Input 'exit' to quit this command.")
        else:
            return chk_num

    def set_end(self, end):
        self.end = end

    def in_range(self, chk_num):
        return (not self.start or self.start <= chk_num) and \
               (not self.end or self.end > chk_num)

    def start_check_num(self, chk_type='id'):
        while 1:
            chk_num = input('Please input %s:' % chk_type)
            if chk_num == 'exit':
                print('quit')
                return
            parsed_num = self.is_int(chk_num)
            if parsed_num:
                if chk_type != 'money':
                    parsed_num -= 1
                    if self.in_range(parsed_num):
                        return parsed_num
                    else:
                        print('The id number inputted is not in correct range. Input exit\' to quit this command.')
                else:
                    return parsed_num


class ProductList(object):
    def __init__(self, init_lst):
        self.products = init_lst
        self.checker = NumChecker(0, len(self.products))

    def show_products(self):
        print('Here\'s the products list, please input product number. Input "exit" to quit')
        print('%-5s%-10s' % ('id', 'product'))
        for i, p in enumerate(self.products):
            print('%-5s%-10s'%(i + 1, p))

    def get_single_product_by_id(self):
        pro_id = self.checker.start_check_num()
        if pro_id is not None:
            return self.products[pro_id]


class Customer(object):
    def __init__(self, products):
        self.shopping_cart = ShoppingCart(products)
        self.property = 0
        self.checker = NumChecker(0)
        self.products = products

    def add_property(self):
        money = self.checker.start_check_num('money')
        if money:
            self.property += money

    def add_commodity(self):
        self.shopping_cart.add_commodity()

    def rmv_commodity(self):
        self.shopping_cart.rmv_commodity()

    def buy_all(self):
        if self.shopping_cart.get_sum_price():
            if self.property >= self.shopping_cart.get_sum_price():
                print('Success')
                return True
            else:
                print('You don\'t have enough money')
        else:
            print('Empty shopping cart')

    def get_product_list(self):
        self.products.show_products()

    def show_shopping_cart(self):
        self.shopping_cart.show_cart_commodities()

    def show_property(self):
        print(self.property)


class ShoppingCart(object):
    def __init__(self, products_obj):
        self.cart = dict()
        self.products_obj = products_obj
        self.checker = NumChecker(0)

    def check_valid_pro(self):
        return self.products_obj.checker.start_check_num()

    def add_commodity(self):
        pro_id = self.check_valid_pro()
        if pro_id is not None:
            if pro_id not in self.cart:
                self.cart[pro_id] = [1, (self.products_obj.products[pro_id]['name'], self.products_obj.products[pro_id]['price'])]
            else:
                self.cart[pro_id][0] += 1
        self.checker.set_end(len(self.cart))

    def rmv_commodity(self):
        if self.cart:
            print('Here\'s the commodities in your chart, please input commodity id.')
            self.show_cart_commodities()
            com_id = self.checker.start_check_num()
            if com_id is not None:
                key = tuple(self.cart.keys())[com_id]
                self.cart[key][0] -= 1
                if not self.cart[key][0]:
                    del self.cart[key]
            self.checker.set_end(len(self.cart))
        else:
            print('Empty shopping cart')

    def show_cart_commodities(self):
        print('%-5s%-10s%-10s%-10s' % ('id', 'product', 'counts', 'price'))
        for i, com_id in enumerate(self.cart):
            print('%-5s%-10s%-10s%-10s' % (i + 1,  self.cart[com_id][1][0], self.cart[com_id][0], self.cart[com_id][1][1]))

    def get_sum_price(self):
        sum_p = 0
        for i in self.cart:
            sum_p += self.cart[i][0] * self.cart[i][1][1]
        return sum_p
