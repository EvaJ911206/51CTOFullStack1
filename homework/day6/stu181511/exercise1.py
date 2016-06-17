from argparse import ArgumentParser
import re


class Calculator(object):
    opt_dict = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    priority_dict = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }

    def __init__(self, expression):
        self.ptn_sub_exp = re.compile(r'\(([^()]+)\)')
        self.split_exp = re.compile(r'(\d+\.\d+|\d+)')
        self.expression = expression.replace(' ', '')

    def get_res(self):
        result = 0
        while 1:
            sub_exps = self.ptn_sub_exp.split(self.expression, 1)
            if len(sub_exps) is 3:
                before_exp, cur_exp, after_exp = sub_exps
                self.expression = before_exp + self.calculate_sub(cur_exp) + after_exp
            else:
                return self.calculate_sub(self.expression)

    def _is_operter(self, chr):
        return chr in ('+', '-', '*', '/')

    def _split_exp(self, cur_exp):
        pos_neg_flag = None
        res = [i for i in self.split_exp.split(cur_exp) if i]
        # if the 1st character is - or +
        # we should parse it first
        # because it's length is only 1
        if self._is_operter(res[0][0]):
            pos_neg_flag = res[0]
            res = res[1:]
        return res, pos_neg_flag

    def _get_pol_cal(self, cur_exp):
        pol_stack = list()
        opt_stack = list()
        res, pos_neg_flag = self._split_exp(cur_exp)
        for i in res:
            if not self._is_operter(i[0]):
                # use eval to turn number with
                # string type into int or float
                pol_stack.append(eval((pos_neg_flag + i) if pos_neg_flag else i))
            else:
                if len(i) > 1:
                    # length of element is larger than 1
                    # means that there is a negative
                    # or positive sign in it
                    pos_neg_flag = i[1]
                    i = i[0]
                else:
                    pos_neg_flag = None
                if opt_stack \
                        and self.priority_dict[i] <= self.priority_dict[opt_stack[-1]]:
                    while opt_stack \
                            and self.priority_dict[i] <= self.priority_dict[opt_stack[-1]]:
                        pol_stack.append(opt_stack.pop())
                opt_stack.append(i)
        pol_stack.extend(opt_stack[::-1])
        #print(pol_stack)
        return pol_stack

    def calculate_sub(self, cur_exp):
        cal_stack = list()
        for i in self._get_pol_cal(cur_exp):
            if not isinstance(i, str):
                cal_stack.append(i)
            else:
                num_1st = cal_stack.pop()
                num_2nd = cal_stack.pop()
                cal_stack.append(self.opt_dict[i](num_2nd, num_1st))
        return str(cal_stack[-1])


def main(expression):
    print(expression)
    caltor = Calculator(expression)
    print(caltor.get_res())

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-t',
                        help='')
    args = parser.parse_args()
    main(args.t)