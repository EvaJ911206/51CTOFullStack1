import re
from TypeChecker import check_obj_type


def print_result(num_count, alpha_count, space_count, other_count):
    print('Got %s numbers' % num_count)
    print('Got %s alphabets' % alpha_count)
    print('Got %s spaces' % space_count)
    print('Got %s other characters' % other_count)


@check_obj_type((str,))
def calculate2(str_ipt):
    p_num = re.compile(r'\d')
    p_alpha = re.compile(r'[A-Za-z]')
    p_space = re.compile(r'\s')
    num_count = len(p_num.findall(str_ipt))
    alpha_count = len(p_alpha.findall(str_ipt))
    space_count = len(p_space.findall(str_ipt))
    other_count = len(str_ipt) - num_count - alpha_count - space_count
    print_result(num_count, alpha_count, space_count, other_count)


@check_obj_type((str,))
def calculate1(str_ipt):
    num_count = alpha_count = space_count = other_count = 0
    for i in str_ipt:
        if i.isdigit():
            num_count += 1
        elif i.isalpha():
            alpha_count += 1
        elif i.isspace():
            space_count += 1
        else:
            other_count += 1
    print_result(num_count, alpha_count, space_count, other_count)


if __name__ == '__main__':
    calculate1('fdaafda12131far243 eew2 qww12***3((')
    calculate2('fdaafda12131far243 eew2 qww12***3((')
    calculate2(12)
