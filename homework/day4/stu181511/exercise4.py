from TypeChecker import check_obj_type


@check_obj_type((str, list, tuple))
def check_space2(ipt_arg):
    chk_lst = [' ', '\r', '\n', '\t', '\v', '\f']
    if not isinstance(ipt_arg, str):
        chk_lst.append(None)
    return any(map(lambda x: x in ipt_arg, chk_lst))


@check_obj_type((str, list, tuple))
def check_space1(int_arg):
    chk_lst = (' ', None, '\r', '\n', '\t', '\v', '\f')
    for i in int_arg:
        # using 'is' is better than isspace,
        # because some type hasn't this function
        if i in chk_lst:
            return True
    return False


if __name__ == '__main__':
    print(check_space1('\rDA'))
    print(check_space1(['DAFA DSEW EW', '1 ', 'da', 12]))

    print(check_space2('\rDA'))
    print(check_space2(['DAFA DSEW EW', '1 ', 'da', 12]))

